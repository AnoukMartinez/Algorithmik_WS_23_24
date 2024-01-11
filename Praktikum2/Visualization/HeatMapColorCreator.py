from bokeh.colors import RGB


class HeatMapColorCreator:
    """
    Class with the responsibility to generate the colors of nodes for a heatMap. 
    Here a maximum value is passed. The colors are then generated based on the deviation from this maximum value.

    Parameters
    ----------
    maximum: The highest number. This is equivalent to R = 255 G=0 B=0, center R = 255 G=0, lowest number R = 0, G =255

    """

    interval = 0

    def __init__(self, maximum):
        """
        Parameters
        ----------
        maximum: highest number equivalent to R = 255 G=0 B=0, center R = 255 G=0, lowest R = 0, G =255
        """
        self.interval = maximum / 510

    def heat_map_color_based_on_max_value(self, value_to_check: int):
        """
        Method with the responsibility to calculate a heat map color (red, yellow, green) based on a deviation from a
        maximum value for a single Node. The maximum value is set in the constructor of this class.


        Return
        ------
        HeatMap Color
        """

        color_value = int(value_to_check / self.interval)

        red_value = 0
        green_value = 0

        if color_value >= 255:
            red_value = 255
            green_value = 510 - color_value

        if color_value < 255:
            red_value = color_value
            green_value = 255

        color = RGB(red_value, green_value, 0, 1)
        return color
