# WikIndex

By Robin Camille Davis (@robincamille), begun 2013, updated 2016

## About 
Who's been written about in books, but not on Wikipedia? Who has an article in a printed encyclopedia, but not on Wikipedia?

This Python script turns text formatted as a typical book's index of names to a list of Wikipedia links, split into columns. This task is useful for creating 'red link lists,' which are usually listed on a Wikipedia user page and are an easy way to visualize who's been written about and who hasn't. (Example: [Women in history](https://en.wikipedia.org/wiki/User:Rcamilled/Redlinks/Women_in_history), red link lists I made using indexes from encyclopedias.)

## How to use
1. Select an index that you can copy/paste from. Encyclopedias and history books are especially great for this.
1. Copy/paste the index into a .txt file
1. On the command line, run this:
```python wikindex.py [inputfilename.txt] [outputfilename.txt]```
1. Copy/paste the text in outputfilename.txt to your Wikipedia user (sub)page, save, and view
1. Manual cleanup: take out obvious errors.
1. Now you're ready to go through the list, name by name, and begin writing biographical articles! 

## Example 
### Raw source to red link list
**Source:** [Raw index in a book about printing history from 1900](http://www.gutenberg.org/files/20393/20393-h/20393-h.htm) (scroll down)
**Output:** [Links on my user page](https://en.wikipedia.org/wiki/User:Rcamilled/Redlinks/Printers#Entities_mentioned_in_Plomer) (I later split them into lists of red & blue links)

### What the script does to text
Turns this, from a plain-text file:
>Abree, J., 253.<br/>Alday. See Alde.<br/>Alde, Edward, 163, 169.<br/>Alde, Elizabeth, 169.<br/>Alde, John, 101, 163.<br/>Allen, Edward, 271.<br/>Allen, John, 220.<br/>

... Into this, outputted into a plain-text file...
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

... Which looks like this on Wikipedia: 

<ul>
<li><a href="/w/index.php?title=Edward_Alde&amp;action=edit&amp;redlink=1" class="new" title="Edward Alde (page does not exist)" style="color:red" >Edward Alde</a></li>
<li><a href="/w/index.php?title=Elizabeth_Alde&amp;action=edit&amp;redlink=1" class="new" title="Elizabeth Alde (page does not exist)" style="color:red" >Elizabeth Alde</a></li>
<li><a href="/w/index.php?title=John_Alde&amp;action=edit&amp;redlink=1" class="new" title="John Alde (page does not exist)" style="color:red" >John Alde</a></li>
<li><a href="/wiki/Edward_Allen" class="mw-disambig" title="Edward Allen" style="color:blue" >Edward Allen</a></li>
<li><a href="/wiki/John_Allen" class="mw-disambig" title="John Allen" style="color:blue" >John Allen</a></li>
</ul>


#### What's happening?
- Page numbers are stripped out.
- Names are flipped from *last, first* to *first last*. 
- Lines like *Alday. See Alde.* are removed. 
- Names with just an initial, like *Abree, J.*, are removed. 
- Titles, like "Dr.", are also removed.

## Caveats 
If your list has 150+ names on it, split it into chunks of 150 names each (so that you don't have more than 5 columns of 30 names in your output page). This will also make it easier to navigate your resulting user page.

This script does not work well with overly-complex indexes or diacritics, sorry :(

Some names might link to a disambiguation page. They'll appear blue, but there still may not be a page for the specific person your index lists. 

Some people's 'canonical' name may be different from how the index lists them, for instance, *Jane Patricia Smith* might be in use instead of *Jane Smith* or *Jane P. Smith*. In this case, it's useful to check and create a redirect page so others can find the person.

## Questions?
List an issue if you have a question or found a problem. 

Submit a pull request if you found a problem and fixed it.

PS. If you use this for something cool, I'd love to hear about it! 

### License 
CC BY-NC