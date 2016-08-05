# WikIndex

By Robin Camille Davis (@robincamille), begun 2013, updated 2016

## About 
Who's been written about in books, but not on Wikipedia? Who has an article in a printed encyclopedia, but not on Wikipedia?

This Python script turns text formatted as a typical book's index of names to a list of Wikipedia links. This task is useful for creating 'red link lists,' which are usually listed on a Wikipedia user page and are an easy way to visualize who's been written about and who hasn't. (Example: [Women in history](https://en.wikipedia.org/wiki/User:Rcamilled/Redlinks/Women_in_history), red link lists I made using indexes from encyclopedias.)

## Example 
### Raw source to red link list
**Source:** [Raw index in a book about printing history from 1900](http://www.gutenberg.org/files/20393/20393-h/20393-h.htm) (scroll down)
**Output:** [Links on my user page](https://en.wikipedia.org/wiki/User:Rcamilled/Redlinks/Printers#Entities_mentioned_in_Plomer) (I later split them into lists of red & blue links)

### What the script does to text
Turns this, from a plain-text file:
> Abree, J., 253.
> Alday. See Alde.
> Alde, Edward, 163, 169.
> Alde, Elizabeth, 169.
> Alde, John, 101, 163.
> Allen, Edward, 271.
> Allen, John, 220.

Into this, outputted into a plain-text file:
```
{{col-begin}}
{{col-break}}
*[[Edward Alde]]
*[[Elizabeth Alde]]
*[[John Alde]]
*[[Edward Allen]]
*[[John Allen]]
{{col-end}}
```

Page numbers are stripped out, and names are flipped from *last, first* to *first last*. Notice that lines like *Alday. See Alde.* were removed, as well as names with just an initial, like *Abree, J.* Titles, like "Dr.", will also be stripped out.

## How to use
1. Select an index that you can copy/paste from. Encyclopedias and history books are especially great for this.
1. Copy/paste the index into a .txt file
1. On the command line and run this:
```python wikindex.py [inputfilename.txt] [outputfilename.txt]```
1. Copy/paste the text in outputfilename.txt to your Wikipedia user (sub)page, save, and view
1. Manual cleanup: take out obvious errors.
1. Now you're ready to go through the list, name by name, and begin writing biographical articles! 

## Caveats 
If your list has 150+ names on it, split it into chunks of 150 names each (so that you don't have more than 5 columns of 30 names in your output page). This will also make it easier to navigate your resulting user page.

This script does not work well with overly-complex indexes or diacritics, sorry.

Some names might link to a disambiguation page. A Wikipedia bot may or may not tell you this eventually. 

Some people's 'canonical' name may be different from how the index lists them, for instance, *Jane Patricia Smith* instead of *Jane Smith* or *Jane P. Smith*. In this case, it's useful to check and create a redirect page so others can find the person.

## Questions?
List an issue if you have a question or found a problem. 

Submit a pull request if you found a problem and fixed it.

PS. If you use this for something cool, I'd love to hear about it! 

### License 
CC BY-NC