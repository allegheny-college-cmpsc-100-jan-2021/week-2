# Worksheet 2.0.f1: The dealership

![G. Wiz: profiting from your work since 2021](https://cs.allegheny.edu/sites/dluman/cmpsc100/cmpsc-100-the-dealership.png)

G. Wiz -- like anyone these days -- is looking for some part-time, passive income. And, like any reasonable person, they've hit on the idea of becoming an art dealer. I mean, people will pay a gazillion dollars for anything _artistic_, right? Despite any experience in the trade, G. Wiz thinks this is a _great idea_.

There's just one big problem: G. Wiz doesn't know any artists, except -- now -- you. G. Wiz is, however, savvy about one thing: trends. And, currently, the Gator Kingdom is all about abstract art. Looking through the local auction house's collection, G. Wiz noticed that the following painting sold for `UNDISCLOSED SUM`, but that probably means it's A LOT OF DOLLARS:

![#ART](https://cs.allegheny.edu/sites/dluman/cmpsc100/cmpsc-100-the-art.png)

## Requirements

This program should create an image which:

* Is `1920` x `1080` pixels large
* Uses at least one of each of the following shapes (more interesting pictures use _many_):
  * `ellipse`
  * `rectangle`
  * `polygon`
    * Here's the ["formal" definition of the method](https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.polygon)
* Adds these shapes using a random approach written in a function
* Has a background other than black or white
* Pastes G. Wiz's picture in the bottom right corner (he has to have a branded picture for the catalog)
  * Use the `g_wiz_mark.png` file located in this directory
  * If you would like to include the picture with a transparency (i.e. no packground), as the last argument of your paste command, add:
  
  ```python
    mask=g_wiz_mark 
  ```
* Is saved in this directory as `the_art.png`
  
When you're done, congratulations -- you just made computational art. (That G. Wiz makes all the profit from.)

## Notes

This work should be completed in the [f1_week-2-worksheet-dealership.py](f1_week-2-worksheet-dealership.py) file. Recall that, during class, this is the way Python development is largely done. While we will still use notebooks like worksheets, when it comes to to real programming jobs, we're going to start getting the habit of programming real programs in *.py files.

There's already some code in the file to get you started.