import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def cartoonize_image(image, num_down=2, num_bilateral=7):
    """
    Convert a normal image into a cartoon-style image.
    Steps:
    1) Smooth large color regions
    2) Extract bold edges
    3) Combine smoothed color and edge mask
    """

    # 1. Smooth color regions
    img_color = image.copy()

    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)

    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)

    img_color = cv2.resize(img_color, (image.shape[1], image.shape[0]))

    # 2. Detect edges
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 7)

    img_edge = cv2.adaptiveThreshold(
        img_gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        2
    )

    # Convert edge image to 3 channels
    img_edge_color = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)

    # 3. Combine color and edges
    cartoon = cv2.bitwise_and(img_color, img_edge_color)

    return cartoon, img_edge, img_color


def save_comparison_image(original, smooth_color, edge, cartoon, save_path="comparison_result.jpg"):
    """
    Save a side-by-side comparison image.
    """
    edge_bgr = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    h, w = original.shape[:2]
    smooth_color = cv2.resize(smooth_color, (w, h))
    edge_bgr = cv2.resize(edge_bgr, (w, h))
    cartoon = cv2.resize(cartoon, (w, h))

    comparison = np.hstack([original, smooth_color, edge_bgr, cartoon])
    cv2.imwrite(save_path, comparison)
    return comparison


def show_with_matplotlib(image_bgr, title="Image"):
    """
    Display image using matplotlib (more stable in Spyder than cv2.imshow).
    """
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 8))
    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis("off")
    plt.show()


def main():
    # ===== Change these paths in Spyder =====
    input_path = "image1.jpg"          # Put your image file here
    output_path = "cartoon_output.jpg"
    comparison_path = "comparison_result.jpg"
    # ========================================

    if not os.path.exists(input_path):
        print(f"[ERROR] Input file not found: {input_path}")
        print("Put your image in the same folder as this script,")
        print("or change input_path to the full file path.")
        return

    image = cv2.imread(input_path)

    if image is None:
        print("[ERROR] Failed to load the image.")
        print("Check the file path or image format.")
        return

    cartoon, edge, smooth_color = cartoonize_image(image)

    # Save cartoon result
    saved1 = cv2.imwrite(output_path, cartoon)

    # Save side-by-side comparison
    comparison = save_comparison_image(image, smooth_color, edge, cartoon, comparison_path)

    if saved1:
        print(f"[INFO] Cartoon image saved: {output_path}")
        print(f"[INFO] Comparison image saved: {comparison_path}")
    else:
        print("[ERROR] Failed to save output image.")
        return

    # Show results in Spyder-friendly way
    show_with_matplotlib(comparison, "Original | Smoothed | Edge | Cartoon")


if __name__ == "__main__":
    main()