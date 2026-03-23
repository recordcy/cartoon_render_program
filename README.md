# cartoon_render_program
A simple OpenCV-based image processing project that converts a normal image into a cartoon-style image.

---

## 1. Description

This program transforms an input image into a cartoon-like rendering using classical image processing techniques in OpenCV.

The goal is to simplify color regions while preserving strong edges, so that the final output resembles a cartoon or comic-style image.

---

## 2. Features

- Convert a normal image into a cartoon-style image
- Emphasize edges while smoothing colors
- Save the final cartoon result
- Generate a comparison image including:
  - Original image
  - Smoothed color image
  - Edge image
  - Cartoon output

---

## 3. How It Works

The algorithm consists of three main steps:

### 1) Color Smoothing
- The image is downsampled using Gaussian pyramids
- Bilateral filtering is applied multiple times
- This reduces noise while preserving edges

### 2) Edge Detection
- Convert image to grayscale
- Apply median blur to remove noise
- Use adaptive thresholding to extract bold edges

### 3) Image Combination
- Combine the smoothed color image with the edge mask
- Produce a cartoon-like effect

---

## 4. Function Description

- `cartoonize_image(image)`  
  Converts the input image into a cartoon-style image by smoothing colors and extracting edges.

- `save_comparison_image(...)`  
  Saves a side-by-side comparison of original, smoothed, edge, and cartoon images.

- `show_with_matplotlib(...)`  
  Displays images using matplotlib (useful in environments like Spyder).

---

## 5. Requirements

- Python 3
- OpenCV
- NumPy
- Matplotlib

Install dependencies:

```bash
pip install opencv-python numpy matplotlib
## 6. How to Run
Step 1: Put your image in the same folder
project/
├─ cartoon_render.py
├─ input.jpg
Step 2: Modify input path in code
input_path = "input.jpg"
Step 3: Run the program
python cartoon_render.py
Note (Spyder Users)

If you are using Spyder, directly edit the input_path variable in the code instead of using command-line arguments.

## 7. Output

The program generates:

cartoon_output.jpg → Final cartoon-style image
comparison_result.jpg → Side-by-side comparison
8. Demo: Good Cases

The algorithm works well when:

The object has clear boundaries
The background is simple
Lighting is uniform
Colors are well separated
Example

## In these cases:

Edges are clearly defined
Colors become flat and smooth
The result looks like a cartoon drawing
9. Demo: Bad Cases

The algorithm performs poorly when:
## 
The background is complex
The image has too many fine textures (hair, grass, leaves)
Lighting is uneven or very dark
The image is noisy
Example

## In these cases:

Too many edges appear
The result looks messy
Cartoon effect is weak
## 10. Limitations

This method has several limitations:

It uses traditional image processing, not deep learning.
It cannot understand semantic regions (e.g., face, sky, background).
Fine textures may produce excessive edges.
Results depend heavily on lighting and image quality.
The output may look like a filtered photo rather than a real cartoon.
