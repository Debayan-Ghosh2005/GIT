use image::{GenericImageView, DynamicImage, Rgba};

fn get_str_ascii(intensity: u8) -> &'static str {
    let ascii = [" ", ".", ",", "-", "~", "+", "=", "@"];
    let index = ((intensity as f32) / 32.0).min(7.0) as usize;
    ascii[index]
}

fn get_image(dir: &str, scale: u32) -> DynamicImage {
    let img = image::open(dir).unwrap();
    let (width, height) = img.dimensions();
    let mut ascii_image = DynamicImage::new_rgba8(width / scale, height / (scale * 2));

    for y in (0..height).step_by(scale as usize * 2) {
        for x in (0..width).step_by(scale as usize) {
            let pix = img.get_pixel(x, y);
            let intensity = (pix[0] as f32 / 3.0 + pix[1] as f32 / 3.0 + pix[2] as f32 / 3.0) as u8;
            let ascii_char = get_str_ascii(intensity);
            for i in 0..scale {
                for j in 0..(scale * 2) {
                    let new_x = (x / scale) + i;
                    let new_y = (y / (scale * 2)) + j;
                    if new_x < width / scale && new_y < height / (scale * 2) {
                        let rgba_pixel = Rgba([
                            pix[0],
                            pix[1],
                            pix[2],
                            if pix[3] == 0 { 0 } else { 255 },
                        ]);
                        ascii_image.put_pixel(new_x, new_y, rgba_pixel);
                    }
                }
            }
        }
    }
    ascii_image
}

fn main() {use std::fs::File;
use std::io::Write;

fn main() {
    // Use raw string literals to avoid escaping backslashes
    let dir = r"C:\Users\DEBAYAN\OneDrive\Desktop\photo_2023-09-24_02-08-31";
    let scale = 4;
    let ascii_image = get_image(dir, scale);

    // Open a file for writing
    let mut file = File::create("ascii_art.txt").expect("Failed to create file");

    // Iterate over the ASCII image and write each line to the file
    for y in 0..ascii_image.height() {
        for x in 0..ascii_image.width() {
            // Get the ASCII character at (x, y)
            let ascii_char = ascii_image.get_pixel(x, y)[0] as char;
            // Write the ASCII character to the file
            file.write_all(ascii_char.to_string().as_bytes()).expect("Failed to write to file");
        }
        // Write a newline character at the end of each row
        file.write_all(b"\n").expect("Failed to write to file");
    }
}

}
