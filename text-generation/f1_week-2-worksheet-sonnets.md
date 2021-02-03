# This sonnet doesn't exist

```
O from what power hast thou this becoming of things 
ill, that thou hast thy will, thy image should keep 
open whereto the judgment that your pity is enough 
to torture me alone, to new-found methods, and 
to temptation slow: But if thou shouldst depart, 
what means the world  enjoys it; Then may I sing, 
No! Time, thou shalt not boast that I have sworn 
deep oaths of thy days, Stealing unseen to west 
with this growing age, yet in good faith some say 
that I cannot blame thee, for my muse, rough winds 
do shake the darling buds of marjoram had stol’n 
of both, When to the heart,That looks on tempests 
and is partly blind, Proving his beauty still.
```

O, that's my favorite of Shakespeare's sonnets -- number 11,341,134.

Well, actually, it's not real. I literally made it this morning. 

And, you're about to make one, too. Our goal for this activity is to see what text generation can do using all of Shakespeare's sonnets (which, for our crude purpose will be defined as a poem of only `14` lines -- metre be damned). Given that we're using a library to do the "heavy lifting," this is actually a very simple process -- though it may take a few tries for you to get something you actually like.

There's already a bit of code in our [python file](f1_week-2-worksheet-sonnets.py) -- I've given you the `markovify` boilerplate. It's up to you to:

* generate the lines using `model.make_short_sentence`, like we did in the [0_week-2-worksheet-text-generation.ipynb](0_week-2-worksheet-text-generation.ipynb) worksheet
* join the lines together in a poem-looking string, that you
* write to a file called `sonnet.txt`

## Note

In today's grader, the line:

```
✔  The command output has exactly 1 of the '13' fragment
```

refers to whether or not `sonnet.txt` has enough lines in it.