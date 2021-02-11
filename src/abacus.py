
class Frame(object):

    def __init__(self, value):
        self.value = value
        self.frame_tops = {0: '|00-',
                           1: '|0-0',
                           2: '|-00'}

        self.frame_bottoms = {0: '|-00000|',
                              1: '|0-0000|',
                              2: '|00-000|',
                              3: '|000-00|',
                              4: '|0000-0|',}
        self.top_divide = int(self.value / 5)
        self.bottom_remainder = self.value % 5
        self.frame_view = self._generate_frame_top() + self._generate_frame_bottom()

    def _generate_frame_top(self):
        return self.frame_tops[self.top_divide]

    def _generate_frame_bottom(self):
        return self.frame_bottoms[self.bottom_remainder]

    def get_frame_view(self):
        return self.frame_view


class Abacus(object):

    def __init__(self, value, places=10):
        self.value = value
        self.places = places
        self.frames = ''
        self.value_list = list(str(self.value))
        while len(self.value_list) < self.places:
            self.value_list.insert(0, 0)

        for i in range(len(self.value_list)):
            frame = Frame(int(self.value_list[i]))
            self.frames = f'{frame.get_frame_view()}\n{self.frames}'

    def get_abacus(self):
        return self.frames




