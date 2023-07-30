import sudoku_solver
import cv2
import pytesseract
import matplotlib.pyplot as plt


def display_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for matplotlib
    plt.imshow(image)
    plt.axis("off")  # Hide the axis
    plt.show()


def extract_digits_and_empty_cells_from_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Resize the image (optional)
    # display_image(image)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply image processing to enhance digit extraction accuracy (you can adjust parameters as needed)
    processed_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find the contours in the processed image
    # contours, _ = cv2.findContours(processed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the bounding box of the outermost contour
    # x, y, w, h = cv2.boundingRect(contours[0])

    # Crop the image to the bounding box of the outermost contour
    # processed_image = processed_image[y:y + h, x:x + w]

    # Use Tesseract for character recognition
    # extracted_text = pytesseract.image_to_string(processed_image, config='--psm 6 outputbase digits')
    extracted_text = ""

    # Calculate the width and height of each cell
    cell_height = processed_image.shape[0] // 9
    cell_width = processed_image.shape[1] // 9

    empty_cells = []
    offset = int((cell_width + cell_height) / 10)

    # Iterate through each cell
    for i in range(9):
        for j in range(9):
            # Calculate the cell coordinates with an offset
            x_start = j * cell_width + offset
            x_end = (j + 1) * cell_width - offset
            y_start = i * cell_height + offset
            y_end = (i + 1) * cell_height - offset

            # Crop the cell image
            cell_img = processed_image[y_start: y_end, x_start: x_end]
            cell_digit = pytesseract.image_to_string(cell_img, config='--psm 6 outputbase digits')
            display_image(cell_img)
            print(cell_digit)

            if cell_digit.strip():
                # If cell contains a digit
                extracted_text += cell_digit.strip()
            else:
                # If cell is empty
                empty_cells.append((i, j))
                extracted_text += "0"

    return extracted_text.strip(), empty_cells


def split_string_into_9x9(string):
    return [string[i:i + 9] for i in range(0, len(string), 9)]


def string_to_2d_list(string_list):
    return [[int(char) if char.isdigit() else 0 for char in row] for row in string_list]


if __name__ == "__main__":
    # Replace with the actual image file path from which you want to extract digits and empty cells
    image_path = "sample_pic/3.jpg"

    extracted_digits, empty_cells = extract_digits_and_empty_cells_from_image(image_path)
    print("Extracted digits:", extracted_digits)
    print("Empty cells:", empty_cells)

    # sudoku_matrix = generate_sudoku_matrix(extracted_digits, empty_cells)
    sudoku_string_list = split_string_into_9x9(extracted_digits)
    sudoku_matrix = string_to_2d_list(sudoku_string_list)

    print("Sudoku Matrix:")
    for row in sudoku_matrix:
        print(row)

    print('-' * 15)
    print("Sudoku Solver:")
    print('-' * 15)

    if sudoku_solver.solve_sudoku(sudoku_matrix):
        for row in sudoku_matrix:
            print(row)
    else:
        print("This Sudoku puzzle has no solution.")
