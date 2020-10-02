""" Albert Ratajczak - 2019
"""
import winreg

def switch_01(value):
    """ Switches 0 to 1 and 1 to 0
        :param value: integer, 0 or 1
        :return: integer, 1 or 0
    """
    if value not in (0, 1): raise ValueError('value has to be equal to 0 or 1')
    return 0 if value else 1


def switch_color_theme():
    """ Switches Windows 10 default app mode between light
        and dark theme by changing value of registry key
    """
    key = winreg.HKEY_CURRENT_USER
    sub_key = r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize'

    # Default app mode registry key: 0 - dark, 1 - light
    theme_key = winreg.OpenKey(key, sub_key, 0, winreg.KEY_ALL_ACCESS)
    theme_key_value = winreg.QueryValueEx(theme_key, 'AppsUseLightTheme')[0]

    # Switching key value: 0 <--> 1
    winreg.SetValueEx(
                  theme_key,
                  'AppsUseLightTheme',
                  0,
                  winreg.REG_DWORD,
                  switch_01(theme_key_value)
                  )

    winreg.CloseKey(theme_key)


if __name__ == '__main__':
    switch_color_theme()
