You have a good basis. Okay? Because you have, like, you have some some results.
Right? But for example, when you say, for example, you have overfitting
challenges, for example.

Right? So you should you should try to see, for example, how you can fight
overfitting. Right? You should try without augmentation, or you should try to
change, with dropout, or let's say, to go so, basically, you should try to go
beyond, okay. I've tried the model and it seems to work.

Right? To maybe do more and say, okay. So this is was the base model. Then I
have added that augmentation, then I've added that one. Right?

And, in in a way to, to show that the because otherwise, the impression is,
okay. I downloaded the model. I tried it. Yeah. It kinda worked, 70%, and and
that's it.

Right? And so this is what you could, actually try to to do. Also, what you
could try to do is, for example, depending a bit on what you like to do, for
example, you could, implement your model, and use it in real time in a web
application, for example. You know? Like, for example, oh, you you recognize
your face.

Right? Because if I remember correctly, your data set was, it's, you okay. You
you recognize a specific celebrity. Right? Okay.

So for example, what you could do is, you could take, for example, do a a demo
with the with the web cam and take the picture of a celebrity of an iPhone on on
the phone and show it to the camera and see that it recognize the phone. Or
apply to maybe, you know, like, some other images that you find on Internet, for
example. Okay. Yeah. Yeah.

Yeah. Yeah. So but but, basically, that's okay. So that that's, but but,
basically, I think that one of the the thing that that it will be important to
see is, like, for example, try to check to fight overfitting. Use maybe that
augmentation.

Use a bit more of those kind of maybe maybe, you know, maybe there are even,
like, I don't remember exactly, what models yep. Yeah. Yeah. Mhmm. Mhmm.

Mhmm. Yeah. Maybe maybe what you can do is, you can, you can use again. So some
maybe documentation, some, I don't know. I would have to search a bit, but, but,
maybe, again so some some, to reduce overfitting, you can do maybe some for
example, you you did some when you say that you, VGG 16, you did some further
training.

I I did I don't remember. Sorry. Or you use it out of the box. Yep. Okay.

So yeah. So what you can do, for example, with g VGG 16, you could also try some
maybe hyperparameter tuning. Let's say, okay. I tried maybe different you know,
when you do transfer learning, maybe you try different number of layers, just to
to try to see, okay. Maybe I can get maybe better or you can show that you have
used, also such methodologies for you know what I mean?

It's like, the classical pipeline is you you take out the box, you get result,
then you you do some transfer learning, then you get result, then you do the
documentation, then you compare the result, then you you try maybe some, some
dropout more, or you try different set of parameters and you do, you do that and
and so on. So to get to a point where you say, okay. I've tried multiple things,
and that's what I, what I I I got. Right? For example, something else that I
would suggest you to do is the following.

When you when you communicate things in the, on slides, for example, one thing
that you should always do, for example, you explain me now that you have done
some further training. Right? So when you when you say that, you should give me
the information about that. So, for example, you have frozen all the layers, and
you have maybe replaced the last two. And the last two has 10 neurons each or
whatever.

Right? You should give me the information about how you did this for the
training. Because when I when I see your slide, they are, like, you know, like,
accuracy of an epoch. I'll show you what I mean. So you should try to be more
precise in in in what you've done.

Okay? Just a second. Let me let me find it. I think it's this one. Yes.

I think it's this one. Right? For example, you use for example, when you say
accuracy of an epoch, and disease this distilled here. So, it's not very clear.
So you should say, for example first of all, you should have, like, labels on
the on the plots.

For example, you should say that put the title here saying these are the plots
of the loss function, blah blah blah, or the accuracy or whatever it is, and you
have epochs. Right? You should also, when you say you're overfitting challenges,
you should say, okay. Now how can I address that? When you plot this one, this
one is fine.

Right? But but the question is, which network have you really trained? Right?
What optimizer have you used, and so on and so forth. So that that I can get an
idea about what you've done.

Right? Because otherwise, it remains kinda you say, okay. I fine tune v g g 16,
but I have no idea how you did it. Right? You say here addition of this layer.

Right? Fine. That's how you do it. Right? But the question is how big were the
the layers?

And you know what I mean? It's like, try to explain, like, all the technical
information that that you have. Right? As much as possible, you have to you can
think it this way. That you should have enough information in there that if I
wanted, I I would be able to redo what you did.

Okay? So in principle, your work, since it's, research work, should be
reproducible. So imagine that you are you are you have to give me enough
information so that I can be doing. Right? So when you when you when you say
here, for example, right, results change with each model training, of course.

Right? But what what do you want to tell me with that? Right? Well, what is the
message? Right?

Overfitting challenges, you should say that, for example, starting from, I don't
know, APOP 20 of overfitting, and you can do it. And the next slide should
contain things like to fight overfitting. I've done that and that and that or
whatever. Right? Also, the the confusion metrics is fine.

Right? Also, like, here, for example, this the you have, like, lots of network
here. Right? So, the question is, for example, if you choose one, why you choose
deep phase? Right?

And then you should also, for example, right, you have here deep phase. Right?
You should always like, when you try multiple model, try to, to make a
comparison. Maybe you can do a a table where you compare different metrics. For
example, the accuracy or the, I don't know, the f one score or whatever.

Right? So when you say, for example, things like special confusion metrics, it's
not clear exactly what you mean. Right? But no. No.

No. No. That I know. I know. I know.

But but the but, you know, you're communicating. I I I agree. I I mean, I'm just
talking for the next ones. Don't don't worry about those ones. Right?

Always think about that, you should have, try to if you have to put, like, a
message, it's fine. Right? But try to to make it so that I have, like, enough
information to to to understand what you've done. Okay? So for example, you try
two models.

Okay. Three models. Sorry. So three models. Right?

When you see when you do comparing three models, right, may you can have the
numbers. Right? But then you should give me some kind of maybe, you know, like,
for example, you have these numbers here. Right? So, yeah, what what I'm trying
to say is that, I think the best probably suggestion I can give you is that the
best the the, the thing that we'll give you probably would would make your
presentation a lot better would be really trying to be as precise as possible
with what you've done.

Okay? So that you can really say, and for example, another thing that you could
you could discuss is, for example, things, you know, another thing that you can
always do is, like, justifying why you choose such models. For example, you
choose DeepFace. Right? Maybe it was, maybe it's the easiest to use out of the
box.

Maybe it's the, according to literature, is the most powerful one. Maybe
whatever reason. Right? So for example, you have the lots of them. Right?

So you could say, so for example, at the beginning, you can say, okay. You want
to, you want to study face recognition. Right? And you what is, for example, of
course, let me to use face recognition model, and you want to compare accuracy
across different models. So the question is how you choose models.

So you could say, okay. I've decided to choose the history model for this
reason, as a metric to compare, use the accuracy, and and so on and so forth.
Right? You know what I mean? Just to make it clear, like, so what you should
have is kind of like, like a story that you are telling.

Right? So for example, you are telling a story and you are explaining me, okay,
this problem is a relevant one. Right? And there are many models. So it's not
always easy to decide which one to choose.

And, and so, like, I decided to compare models so that I can, you know, for
example, decide which model is the more efficient, the easiest to use, whatever
is that you want to do. I decided to as a test to choose between three models.
Maybe one is where I can train myself, one out of the box, and one that is not
deep learning to compare, like, a range of different models. Right? As a
dataset, you decided to use, for example, this one because you have different
people, so you can have, like, different, you know, like, 17 people and so on,
and so on and so forth.

So you kind of try to tell a story behind it. Right? You you have almost
everything there. Right? So I think that the the the important part is how you
link everything together, give enough information, and explain, like, the story
behind behind behind your project.

Right? Yep. Yeah. I would, yeah, I would probably do more, like, at least here,
like, in overfitting, data augmentation. Because, for example, you can take your
dataset and flip the images, rotate the images a bit.

You will see that the that the the the overfitting will go down. Right? If you
have time, I would suggest you try maybe other other one or other two models so
that you have maybe you know, instead of three, you have maybe four or five.
Right? So that you can see, okay.

You know, like, maybe and maybe you can also, give a bit of a for example,
something else that would be interesting to know is, for example, from
literature. Right? Like, how people are doing that? Like, what what what
methods, what networks maybe are are used by people? What kind of accuracy
people get?

Right? Maybe not on your dataset. Right? You take your dataset just as a test.
But it's always good to know state of the art.

Right? For example, maybe the people use that kind of network, and then they
have, like, large data set so that you don't expect this, this accuracy because
your data set is smaller. So I think that if you if you do more with Visual
Studio 16, maybe you try one or two models if you find the time and do some more
update the presentation and maybe do some more, like, state of the art kind of
research. That would be then you have, like, a nice story where you say, okay.
The state of the art is dead.

There are many models, and I chose those for those reasons. And I try and I try
fine tuning. I try it out of the box, and this is the kind of performance that
you get. Right? And then you have your demo that is absolutely fine.

I think that maybe try see if you can if you at at least, like, let me phrase it
this way. At least the thing that state of the art, do some work with v g c 16
and expand the presentation should be doable. Right? If you find the time to add
one or two model, will be great. If you really don't find the time, I think it
will still be okay.

But at least the other parts you should try to do because then it's, you know
but also by reading, like, the state of the art literature, you will maybe find
other ideas. Right? So and you can put your story in a in a wider context, kind
of. Does it make sense? This one?

Yep. The deep phase is no. No. No. I mean, like, maybe you find other models.

Maybe you don't. Just I mean, maybe you can check. If there are, like, other on
GitHub, maybe there is something else. Maybe. I don't know.

You can just check. Just to see for example, it would be, it's always nice when
you when you're choosing something. Right? It's always nice to say, look. Like,
those are the ten ten top kind of models that people use.

Right? And I I I am testing three, and that's absolutely fine. But at least you
give the impression when you're talking or you're presenting that you have
explored the possibilities. Maybe some, models, require too too much GPU or too
too many data with the whatever. But at least you say, okay.

Those are, like, the typical models, right, that people use this. So I chose to
to to check three or four or whatever is that you managed to do. Right? And and
and don't worry about, don't worry about not having, like, having too much text.
You know, I always, I typically don't like very much rules.

What I mean is the following. I think that, it's true in general when you start,
you, you know, you don't want to have a slide that is completely filled with
text. But even that is something that if you have to do to communicate
something, like, scientifically, you need to be sure to have enough information.
So if you have, if you need lots of text, it's fine. I I won't criticize you for
that as long as the text is useful.

You know what I mean? It's like, maybe don't put in pros like, oh, I decided to
do that because at that day, I was feeling that it would itself. But if you
have, like, to say, okay. Those are the metrics. I've chosen this model for this
reason and that and that and that and that, it's absolutely fine.

Don't worry. You know? You can always make boxes around text and maybe organize
text with them. But but but that's I think it's it's less important than the
content at the especially at the beginning. Okay?

And you can you can start. And if you have, like, questions, maybe next week or
in ten days, you let me know. You send me your questions, and we can always
discuss a bit. It's always better to discuss if you have, like, unsure on
something that we if we look quickly together, then, you know, waiting until the
fourth and then maybe, you know, like, because we can always meet ten minutes
and and discuss a few things. Okay.

I would have to leave because I have, like, an info for in ten minutes, so I
have to prepare, like, the the slides. So to prepare the slides to to to
prepare, like, the the presentation I need to present. Is it okay for you now so
far? Perfect. Yeah.

And if you need then anything, then you let me know in the next days and next
week. Perfect. Then then thank you very much, and then I'll talk to you soon.
Bye, everybody.
