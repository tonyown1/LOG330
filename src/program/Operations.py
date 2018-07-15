import math

class Operations:
    """
        Calculates the average 
        @:return will return float representation of average
    """
    def average(self, data):
        list = data
        n = len(data)
        sum = 0
        for x in list:
            sum += x
        return round(float((1/n) * sum), 1)
    """
        Calculates the variance 
        @:return will return float representation of variance
    """
    def variance(self, data):
        list = data
        n = len(data)
        average = self.average(list)
        sum = 0
        for x in list:
            sum += float((x - average)*(x - average))
        return round(float(1/(n-1) * sum), 4)

    """
        Calculates the standard deviation 
        @:return will return the s.d
    """
    def standard_deviation(self, data):
        return round(math.sqrt(self.variance(data)), 2)

    """
        Calculates the correlation
        @:param data list paired with values x, y respectively. 
        @:return will return r and r*r respectively
    """
    def correlation(self, data):
        temp = data
        for d in temp:
            x = d[0]
            y = d[1]
            xx = round(x*x, 2)
            xy = round(x*y, 2)
            yy = round(y*y, 2)
            d.extend([xx, xy, yy])

        n = len(temp)
        sum_x = self.sum_column(temp, 0)
        sum_y = self.sum_column(temp, 1)
        sum_xx = self.sum_column(temp, 2)
        sum_xy = self.sum_column(temp, 3)
        sum_yy = self.sum_column(temp, 4)

        numerator = n*sum_xy - sum_x*sum_y
        denominator = math.sqrt((n*sum_xx - sum_x*sum_x)*(n*sum_yy-sum_y*sum_y))

        r = numerator/denominator

        return [r, r*r]

    """
        Calculates the regression 
        @:param data list paired with values x, y respectively. 
        @:return will return the coefficients b1 and b0 respectively.
    """
    def regression(self, data):
        temp = data
        for d in temp:
            x = d[0]
            y = d[1]
            xx = round(x*x, 2)
            xy = round(x*y, 2)
            d.extend([xx, xy])
        n = len(temp)
        avg_x = self.average(self.get_column(temp, 0))
        avg_y = self.average(self.get_column(temp, 1))
        sum_xx = self.sum_column(temp, 2)
        sum_xy = self.sum_column(temp, 3)

        b1 = (sum_xy-n*avg_x*avg_y) / (sum_xx-n*avg_x*avg_x)
        b0 = avg_y-b1*avg_x

        return [b1, b0]

    """
        Returns the sum of a specified column
        @:param data list paired with values x, y respectively. 
        @:param c the column to sum up.
        @:return will return the sum of the column
    """
    def sum_column(self, data, c):
        sum = 0
        for r in range(len(data)):
            sum += data[r][c]
        return sum
    """
        Returns a single column 
        @:param data list paired with values x, y respectively. 
        @:param c the column number
        @:return will return the column specified
    """
    def get_column(self, data, c):
        temp = []
        for r in range(len(data)):
            temp.append(data[r][c])
        return temp