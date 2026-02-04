# 🖼️ ASCII Art Generator (Python)

A simple **ASCII Art Generator** built using **Python** and **Pillow (PIL)**.  
This program converts an image into ASCII characters based on pixel brightness and saves the result as a text file.

---

## ✨ Features

- 🖼️ Converts images into ASCII art
- 📏 Customizable output width
- 🎨 Grayscale-based pixel mapping
- 💾 Saves ASCII art to a `.txt` file
- 🧑‍💻 Simple command-line interface

---


---

## 🛠️ Requirements

- Python **3.x**
- Pillow (Python Imaging Library)

Install Pillow using:
pip install pillow
---

## ▶️ How to Run

1. Download or clone the project
2. Open terminal / command prompt
3. Navigate to the project directory
4. Run the program:
python ASCII_Art_Generator.py

---

## 🧠 How It Works

### Image Processing Steps

1. **Load Image**
   - Resizes image while maintaining aspect ratio
2. **Convert to Grayscale**
   - Simplifies pixel intensity values
3. **Map Pixels to ASCII**
   - Dark pixels → dense characters  
   - Light pixels → sparse characters
4. **Generate ASCII Art**
   - Formats ASCII characters into lines
5. **Save Output**
   - Writes ASCII art to a text file

---

## 🔤 ASCII Character Mapping
@ % # * + = - : . (space)
- Darker pixels use characters like `@` and `%`
- Lighter pixels use characters like `.` and space

---

## 🧩 Technologies Used

- Python
- Pillow (PIL)

---

## 🚀 Future Enhancements

- Colored ASCII art
- Direct terminal preview
- Support for different ASCII character sets
- GUI version using Tkinter
- Automatic output filename generation

---

## 👤 Author

**Shahid Farhan**  
Python mini-project for image processing and ASCII visualization.

