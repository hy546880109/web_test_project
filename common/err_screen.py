def errorScreen(func):
    def wrapper(self, *args, **kwargs):
        try:
            func(self)
        except:
            self.driver.get_screenshot_as_file('./err_png/{}.png'.format(func.__name__))
    return wrapper
