# -*- coding: utf-8 -*-

class WeatherSearch(object):

    def __init__(self,input_daytime):
        self.input_daytime = input_daytime

    def search_visibility(self):
        visible_leave = 0
        if self.input_daytime == 'daytime':
            visible_leave = 2
        if self.input_daytime == 'night':
            visible_leave = 9

        return visible_leave

    def search_temperature(self):
        temperature = 0
        if self.input_daytime == 'daytime':
            temperature = 26
        if self.input_daytime == 'night':
            temperature = 16
        return temperature

#子类继承父类，并重写父类的search_temperature()方法
class OutAdvice(WeatherSearch):

    def __init__(self,input_daytime):
        WeatherSearch.__init__(self,input_daytime)

    def search_temperature(self):
        vehicle = ''
        if self.input_daytime == 'daytime':
            vehicle = 'bike'
        if self.input_daytime == 'night':
            vehicle = 'taxi'
        return vehicle

    def out_advice(self):
        visible_leave = self.search_visibility() #必须是self.search_visibility()否则search_visibility()找不到对应的方法
        if visible_leave == 2:
            print('The weather is good,suitable for use %s.'%self.search_temperature())
        elif visible_leave == 9:
            print('The weather is bad,suitable for use %s.'%self.search_temperature())
        else:
            print('The weather is beyond my scope.')

if __name__ == '__main__':

    check = OutAdvice('daytime')
    check.out_advice()