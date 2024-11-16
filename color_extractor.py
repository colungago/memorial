import colorgram

class ColorExtractor:
    def __init__(self, path: str, num_of_colors: int):
        self.path = path
        self.num_of_colors = num_of_colors
        self.rgb_colors: list = []
        self.color_proportions: list = []
        self.extract_colors()

    def extract_colors(self):
        colors = colorgram.extract(self.path, self.num_of_colors)
        total_pixels = sum(color.proportion for color in colors)
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            new_color = (r, g, b)
            self.rgb_colors.append(new_color)
            proportion = color.proportion / total_pixels
            self.color_proportions.append((new_color, proportion))

    def get_color_proportions(self):
        return self.color_proportions
