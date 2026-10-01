import colorgram

rgb_colours =[]
# # Extract 30 colors from an image.
colors = colorgram.extract('image.jpg', 30)  #list of objects

 for c in colors:

      r=c.rgb.r #object colors ke and object rgb uske ander attribute r
      g=c.rgb.g
      b=c.rgb.b
      new_colour= (r,g,b)
      rgb_colours.append(new_colour)
 
print(rgb_colours)

#copy the output in  main.py as a colour_list
