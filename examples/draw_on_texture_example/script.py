from nider.core import Font
from nider.core import Outline

from nider.models import Header
from nider.models import Paragraph
from nider.models import Linkback
from nider.models import Content
from nider.models import TwitterPost


# TODO: change this fontpath to the fontpath on your machine
roboto_font_folder = '/home/ovd/.local/share/fonts/Roboto/'

outline = Outline(2, '#121212')

header = Header(text='Your super interesting title!',
                font=Font(roboto_font_folder + 'Roboto-Bold.ttf', 30),
                text_width=40,
                align='left',
                color='#ededed'
                )

para = Paragraph(text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 font=Font(roboto_font_folder + 'Roboto-Medium.ttf', 29),
                 text_width=65,
                 align='left',
                 color='#ededed'
                 )

linkback = Linkback(text='foo.com | @username',
                    font=Font(roboto_font_folder + 'Roboto-Bold.ttf', 24),
                    color='#ededed'
                    )

content = Content(para, header, linkback)

img = TwitterPost(content,
                  fullpath='result.png'
                  )

# TODO: change this texture path to the texture path on your machine
img.draw_on_texture('texture.png')
