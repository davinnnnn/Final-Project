import easyocr

# Function to get the Y-coordinate of the top-left corner of the bounding box
def get_top_left_y_coordinate(bbox):
    top_left = bbox[0]
    return top_left[1]  # Returning the Y-coordinate

# Create a reader instance with Korean and English
reader = easyocr.Reader(['ko', 'en'])

# Path to the image file
image_path = '/content/drive/MyDrive/want_screenshot.jpg'  # Update this to your image file path

# Read the text from the image
results = reader.readtext(image_path)

# Sort results by the Y-coordinate of the top-left point of the bounding box
sorted_results = sorted(results, key=lambda x: get_top_left_y_coordinate(x[0]))

# Extract and print all text, now sorted in reading order
all_text = [text for bbox, text, prob in sorted_results]
clean_text = "\n".join(all_text).strip()  # This will give you clean, organized text

print(clean_text)
