


# Big Title (a line below is added automatically)
## Medium Title
### Small Title
#### Tiny Title
This is a main body text. **This is a bold sentence.** __This is another bold sentence.__  *This is a italic sentence.* _This is another italic sentence._

A new line is created by a newline inserted above. 

<span style="color:red"> Markdown doesn't support text color but allows coloring with HTML style like this. </span> <span style="color:green">See the figure and the link in the sections below for the full HTML color names. </span>

Add a line by "---" (note the newline):

---


# Lists
Bullet points with `-`:
- This is the first point.
- This is the second point.

or with `*` (but don't use them together):
* This is the first point.
* This is the second point.


Sorted list ("`<number>.<one space>`"):

2. The number for the first one decides the start.
999. The actual number displayed will be corrected automatically.
10. This is the third item. It **won't** be sorted in the display according to the number.


Nested lists: starting the nested list at the column of first character of the item of the parent list:
- 12345
  - nested list
- 123456789
  - 12345
    - another nested list
      - one another nested list


Quotations:
> This is the quotation, which could span
> several lines if necessary



# Codes

Codes can be specified like `print('Hello world!') ` using backticks (the one above tab key). 

Create code blocks by three backtics:
```
print('Hello world!')
```
or just using tabs (note the newline before tabs):

    print('Hello world')
    print('Another line of codes')




# Table
You can create a table by creating many `|-|` indicating the number of columns (note that line can be inserted by one or many `-`):
| | column 1 | column 2 |
|-------|---------|-|
| row 1 | content | content |
| row 2 | content | content |
| row 3 | content | content |
| row 4 | content | content |



# Links and Figures
This is an example for internet link that links to [the HTML color names](https://www.codestackr.com/blog/html-color-names/). 
And [another website](https://htmlcolorcodes.com/color-names/) for HTML color is also great.

Links for sections in the same markdown file can be done liek this: [link to the section Table](#table). 

Note that there is always just one `#` in the parentheses, and letters and spaces should be transformed to lower cases and hyphens: [link to the section Links and Figures](#links-and-figures).

Link to a file can be done similarly: [link to the example txt file](./example_file_for_link.txt).

Link to a local figure (note the `!` before brackets): 
![this text will not be shown unless the image fails to load. Typically people add description of the image here.)](./matplotlib_color_name.webp)

You can also link to a online figure in the same way: 
![Github image](https://myoctocat.com/assets/images/base-octocat.svg)




# Helpful References
* [Markdown Cheatsheet on Github](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 
* [Guide to Markdown for Documentation Writers](https://document360.com/blog/introductory-guide-to-markdown-for-documentation-writers/#p8)
* [Markdown Crash Course by Traversy Media](https://www.youtube.com/watch?v=HUBNt18RFbo)
* [Basic Markdown Introduction and Syntax by Mike Dane](https://www.youtube.com/watch?v=2JE66WFpaII)