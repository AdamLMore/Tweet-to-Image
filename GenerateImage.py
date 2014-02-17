from PIL import  Image
import ImageFont, ImageDraw
import TwitterTweetRequester
import textwrap

search_term = "#JustDoIt"

im = Image.new('RGB', (600,350), (64,153,255))

draw = ImageDraw.Draw(im)

#Prepate initial drawing stuff
white = (255,255,255)
text_pos = (10,10)
font = ImageFont.truetype("OpenSans-Regular.ttf", 16)


#Fetch and format the text from a tweet
text = TwitterTweetRequester_PRIVATE.requestTweets(search_term, 1)
text = str(text).encode('ascii')
drawable_text = text.splitlines()

#Draw Author of Tweet
draw.text(text_pos, "@"+drawable_text[0]+":", fill=white, font=font)


#Draw rest of Tweet
offset = 0
for line in textwrap.wrap(drawable_text[1], width=38):
    text_pos = (10,38+offset)
    font = ImageFont.truetype("OpenSans-Regular.ttf", 30)
    draw.text(text_pos, line, fill=white, font=font)
    offset += 32

del draw

#Save image out
im.save('tweet.png', 'PNG')

