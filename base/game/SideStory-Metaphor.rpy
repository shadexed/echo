# Metaphor (revised)
# by Zeke

label sidestory_metaphor:

stop music fadeout 3.0
scene bg black
with slow_dissolve

play background "warehouse.ogg" fadein 10
$ renpy.pause(1, hard=True)
call sidestory_title("Сентябрь 2014") from _call_sidestory_title_2
pause
call sidestory_title("Сентябрь 2014", end=True) from _call_sidestory_title_3

scene bg warehouseint with medium_dis


show Flynn Annoyed at center
"Чешуя блестит от пота, который виден сквозь расстегнутую рубашку, Флинн спускает несколько коробок с рольганга."
"Ящер бодро шагает к своему паллетному домкрату, энергично качая его."
"Он тащит сложенный штабелями поддон с пятнадцатью упаковками двадцатичетырехграммовых бутылок с родниковой водой через склад к прицепу грузовика."
"Опустив поддон, он тащит домкрат обратно, бессистемно бросая его на полпути, когда добирается до прилавка."
show Flynn with dis
"Он берет блокнот, отмечая только что выполненную работу, внимательно изучая список."
"Его хвост мотается туда-сюда, оранжевые пятна выглядят металлическими в скудном свете ламп накаливания."
"Он работает по ночам в этом распределительном центре уже почти восемь лет, но почему-то до сих пор не отвык от этого."
"Флинн кладет планшет на стойку, похлопывает по карманам своими чешуйчатыми когтями и достает пачку сигарет и зажигалку."
"Шон, броненосец, видит, как он идет к боковому выходу."
se "\"Куда это ты собрался?\""
f "\"На перерыв.\""
"Шон потирает лицо обеими лапами."
se "\"Хорошо. Ты действительно делаешь это сегодня? Ты же знаешь, что у нас осталось еще четыре трейлера, верно?\""
"Флинн вставляет сигарету между губ."
f "\"Да, и у нас еще пять часов в чертовой смене. Я вернусь.\""
se "\"Ты - старший смены.\""
f "\"Ты знаешь, где меня найти.\""

scene bg warehouseext with {"master": Fade(0.5, 0.1, 0.3)}
show nightoverlay
show Flynn at left behind nightoverlay

play background2 "parkinglotnocarts.ogg" fadein 5
stop background fadeout 8


"Флинн прислонился к зданию, с незажженной сигаретой во рту, возится с зажигалкой."
"Она искрит, снова и снова, но так и не загорается."
"Он вздыхает, кладет зажигалку обратно в карман и меняет ее на телефон."
$ vol("loop", 0.5)
play loop "engine.ogg" fadein 3
"Он пролистывает несколько постов в социальных сетях, проверяет сообщения, безучастно смотрит на домашний экран."
$ vol("loop", 1, 3)
"Он прислушивается к отдаленному гудению."
"Он различает знакомый пикап на другой стороне парковки и приветствует его, когда тот подъезжает."
stop loop fadeout 3
show Flynn:
    ease 0.6 xalign 0.1
f "\"Вовремя. Ты был слишком занят, чтобы смотреть на луну?\""
show Leo behind nightoverlay with medium_dis:
    xalign 0.95
    yalign 1.0
l "\"Тебе бы это понравилось.\""
l "\"Тебе просто повезло, что я не спал, иначе тебе не с кем было бы поговорить о дерьме.\""
show Flynn Teasing1 with dis
"Флинн хихикает."
show Leo Neutral with dis
"Лео кивает головой в сторону морды ящера."
l "\"Я думал, ты больше не куришь?\""
show Flynn Surprised with dis
"Флинн вынимает сигарету изо рта."
show Flynn with dis
f "\"А. Да, не курю.\""
show Leo Questioning with dis
l "\"...Так что, тебе просто нравится их жевать?\""
"Флинн прочищает горло."
f "\"Э... Да, вообще-то.\""
l "\"...Ладно, мужик. Будет здорово, если ты уволишься, но ты же знаешь, что мне все равно, что ты будешь делать?\""
show Flynn Annoyed with dis
f "\"Нет... А, за...\""
show Flynn with dis
"Он выпустил вздох."
show Flynn Sheepish with dis
f "\"Я серьезно, я бросил. Я их не зажигаю.\""
f "\"Это как... ты держишь вещь, которая убивает тебя между зубами, или что-то вроде того. Это из фильма.\""
show Leo with dis
l "\"...Это действительно чертовски пошло, чувак.\""
show Flynn with dis
"Флинн убирает сигарету в карман и пожимает плечами."
f "\"Да. Не знаю, наверное, мне просто понравилось.\""
"Лео закатывает глаза, издавая вздыхающий смех. Он закидывает лапы за голову и прислоняется спиной к зданию рядом с Флинном, глядя на полную луну."
"Он протягивает лапу и нежно проводит ею по шипам головы ящера."
show Flynn Happy with dis
"Рептилия на мгновение закрывает глаза, мурлыча от прикосновения."
"Он смотрит на сверкающий кусочек серебра на запястье волка, сияющий в лунном свете."
"Лео тоже смотрит, их взгляды ненадолго встречаются."
show Flynn Teasing1 with dis
"Флинн хихикает."
f "\"Твои глаза чертовски странные.\""
f "\"Ты говоришь, что они карие, но на свету они всегда кажутся красными.\""
l "\"Ха. Да, мне это уже говорили.\""
"Лео тянет лапу назад."
f "\"Цк. Почему ты остановился? Ты же знаешь, мне нравится, когда гладят мою спину.\""
show Leo Surprised with dis
l "\"О, э, моя вина?\""
f "\"Я просто прикалываюсь над тобой.\""
show Leo with dis
l "\"У тебя действительно хорошее настроение.\""
show Flynn Happy with dis
f "\"Хех. Да, эм, просто жаждал прикосновений, я думаю.\""
show Leo Wry with dis
l "\"Оу. Я тебе так нужен, да? Хочешь, чтобы объятия на работе стали регулярными?\""
show Flynn Teasing1 with dis
f "\"Успокойся. Я могу получить лучший хвост, чем у тебя, когда захочу.\""
show Leo with dis
l "\"Иди нахуй.\""
f "\"Назови время и место.\""
"Они смеются некоторое время."
"Они погружаются в уютную тишину, слушая звуки, глядя на небо."
show Flynn with medium_dis
f "\"Итак.\""
f "\"Он заканчивает обучение примерно через год, верно?\""
f "\"У нас должно быть что-то вроде встречи выпускников?\""
"Лео прислонился спиной к зданию."
l "\"Угу! Дженна и Тидж тоже.\""
l "\"Захватывающе, правда? Мы снова станем командой, как тогда.\""
f "\"Конечно.\""
"Флинн вынимает сигарету обратно и немного покручивает ее в пальцах, а затем возвращает в рот."
show Leo Neutral with dis
l "\"Ты не выглядишь таким уж взволнованным.\""
"Флинн держит ее во рту, когда говорит."
f "\"Последние несколько лет у нас были разные жизни, Лео.\""
f "\"И многое произошло, некоторые из них... ну, ты знаешь. Кое-что из этого - хуйня.\""
f "\"Просто не удивляйся, если они будут не такими, как раньше.\""
show Leo Depressed with dis
"Лео вздыхает."
l "\"Может быть.\""
l "\"В любом случае. По крайней мере, будет приятно увидеть всех снова.\""
f "\"Конечно.\""
show Flynn Depressed with medium_dis
"Флинн достает пустую зажигалку обратно."
"Он ударяет по ней раз, два, как и много раз до этого, когда он нервничал или ему просто нужно было чем-то занять руки."
"Он смотрит, как искры танцуют и умирают, отчаянно ищет газ, но так и не находит."
"Он вынимает сигарету изо рта, отводя взгляд от волка."
"Он вдыхает."
f "\"И мне нужно знать, где мы находимся, Лео.\""
f "\"Я не хочу снова оказаться в центре этого дерьма. Никто из нас не хочет.\""
"Плечи красного волка опускаются, и он выпускает рваный вздох."
"Он проводит лапой по морде, протирая глаза большим пальцем, затем оглядывается на возвышающуюся рептилию."
show Leo Neutral with dis
l "\"Я люблю тебя и Чейза как {i}друзей.{/i} Очень хороших друзей.\""
show Flynn with dis
l "\"Мне этого достаточно.\""
"Флинн изучает решительное выражение лица Лео."
"Он кладет сигарету обратно в рот."
"Когда он снова заговорил, речь была ровной, почти монотонной."
f "\"Я думаю, это хорошо."
f "\"Если это все, что ты хочешь.\""
l "\"Что ты имеешь в виду?\""
"Флинн пожимает плечами."
f "\"Ничего.\""

$ stop_all_audio(reset=True)
scene bg black
$ renpy.pause(2.5, hard=True)
$ renpy.end_replay()

# # Metaphor (original)
# # by Zeke
#
# September 2014
#
# Scales glistening with perspiration, seen through his open button down shirt, Flynn hefts some boxes down the roller conveyor. The gila reptile then briskly walks over to his pallet jack, pumping it vigorously before dragging the stacked up pallet of fifteen packs of twenty-four count spring water bottles across the stockroom to the truck’s trailer. He dumps the pallet in, then drags the pallet jack out, haphazardly abandoning it mid walk as he gets to the clerical counter under the incandescent bulbs. Flynn picks up a clipboard, checking off the stock he just put on the trailer, going over the list intently. His tail flicks to and fro, the orange splotch patterns looking metallic in the sparse light. He’d been working overnights at this distribution center for nearly eight years, and for some reason hadn’t grown numb to it. Like most things, he normally would. After a while Flynn would stop caring so much about something so routine, and either stop putting so much effort into it, or
# stop doing it altogether. “In fact…” Flynn plops down his clipboard onto the counter, patting his pockets with his scaled claws. He reaches into either side pocket, pulling out a full pack of worn out cigarettes from one pocket, and a zippo lighter from the other. “…Time for a break”, Flynn says under his breath, then walks toward the side exit. Sean, an armadillo, sees him. He sets down a box, walking toward the reptile, “Hey Flynn, where you think you’re going?”
#
# “I’m on break. I’ll be back… Whenever”
#
# Sean rubs his face with both paws, sighing heavily, “Okay; You’re really doing this tonight? You know we still got four trailers left to fill right?”
#
# Flynn pops a cigarette between his lips, “Yeah and we still got five hours in the fuckin’ shift. I’ll be back”
#
# He continues to walk to the door. Sean steps forward a few steps, calling after Flynn, “But you’re the shift lead!” The gila monster continues his journey through the door, turquoise eyes glinting in the dark as he goes through, “You know where to find me.” The metal door closes behind him.
#
# Cigarette dangling from his lip, Flynn futilely tries lighting it with the zippo. It sparks, over and over again, never igniting. He sighs, slipping the lighter back into his pocket, and in return his paw comes back with a cell phone in hand. He checks his messages, scrolling through a few posts on his social media. He perks up at some distant revving, his forked tongue darting out past his unlit cigarette.
#
# “There he is. Fucker”
#
# A rusty pickup truck pulls up near Flynn, who haughtily greets it, “About time. Were you too busy fapping at the moon, slut wolf?”
#
# Leo steps out of the truck, a slightly annoyed smile on his muzzle, “Psh, you’re one to talk about ‘slut’, lizard. You’re lucky I just so happened to be up, otherwise you’d have no one to shit talk to”
#
# Flynn chuckles, pulling out his lighter again as Leo leans against the wall space beside him. The timber wolf raises a brow. “Thought you gave up smoking?”
#
# “I did”, he said holding the lighter. He pulls out the tattered pack of cigarettes “This lighter; it’s empty. This pack; it’s the same one from back then”
#
# Leo gives the reptile a look of awe, “That old!? Jeez… But why? If you really did quit, then why keep those around?”
#
# Flynn puts away the pack and the lighter, taking the cigarette out of his mouth. He turns to Leo holding the cigarette up “As a reminder.”
#
# The wolf tilts his head to the side, “Que?”
#
# Flynn continues “It’s to serve as a reminder of my past, and show that I’m in control. I could smoke these any time if I really wanted, but I quit cold turkey, and made that addiction my bitch”
#
# Leo, turns up his mouth, raising a brow as he looks at Flynn. Flynn chuckles again, “It’s something I saw from a movie a while back. I thought it was kinda deep, meaningful. Figured it wouldn’t hurt to try. Turns out it helped me.”
#
# Leo snorts shaking his head, “Well it sounds either really pretentious or really gay, even for you”
#
# “Why can’t it be synonymous?”
#
# The red wolf rolls his eyes, letting out a sighing laugh. He puts his paws behind his head leaning back against the building, looking up at the full moon. “Why do we even hang out if all our conversations end up like this?”
#
# Flynn rolls the cigarette around his lips, “Conversations are a two-way street, Leo. I didn’t exactly twist your arm to come here. For me, maybe it’s like this cigarette.”
# They stand in silence for a few seconds, looking up at the night sky. Leo reaches over smoothing a paw over Flynn’s head spines, “I dunno Flynn. It just sounds like you’re hanging onto the past.”
#
# The reptile closes his eyes for a moment, then looks over at the glinting piece of silver on the wolf’s wrist. That anchor shining in the moonlight. Leo looks too, their eyes locking briefly, turquoise staring into red. Flynn snickers a bit, “Your eyes are stupid. You say they’re brown, but they always look red in the light.”
#
# “Ha, yeah. I’ve been told that before…” Leo slowly pulls his paw back.
#
# Flynn looks over the wolf,clicking his tongue “Tsk… why’d you stop? You know I like having my spines petted.
#
# Leo’s ears stand on end, then lower slightly “Oh! Well uh… I figured I’d just stop? I dunno…”
#
# The reptile smirks, “I’m just messing with you, slut wolf.”
#
# “Dammit, Flynn. Will you stop calling me that?”
#
# “Maybe. So he’s graduating in about a year now right? We’re supposed to be having some sort of reunion?”
#
# Leo smiles, going back to his recline against the building, “Mhm! Exciting right? We’ll be a crew again, just like back then.”
#
# Flynn scoffs, “And you said I’m the one holding on to the past”
#
# “Fuck you, lizard”
#
# “Name the time and place”
#
# “Épale!” Leo pushes off the wall, standing to face Flynn, “What’s with you tonight? I came to keep you company on your break and-”
#
# Flynn stands from the wall as well, squarely facing Leo. The gila monster has a few inches on the wolf, and it always gave Leo some pause, but never fully intimidated him. They’d done their share of physical squabbles, and while Flynn is a force to reckon with, Leo was clearly more capable. Flynn pulls the cigarette from his maw, “I need to know where we stand, Leo. I don’t wanna get caught in the middle of that shit again. None of us do”
#
# The red wolf’s shoulders ease down as he lets out a ragged sigh. He smooths a paw up his snout, rubbing his eyes with his finger and thumb, then looks back at the towering reptile, “I love you and Chase as friends. Very good friends. That’s good enough for me.”
#
# Flynn rubs his scaly chin, studying the determined look on Leo’s face, “I guess that’s okay. If that’s all you want”
#
# Leo’s ears perk and twitch “Que? What do you mean?”
#
# “Nothing,” Flynn flicks at his lighter again, then puts it away, pulling out another. This time it’s a standard gas station disposable lighter, orange casing. He flicks it, and it immediately ignites. Taking the cigarette out of his mouth he slips it away, patting his khaki pockets, “Damn. Left my loud. Really coulda used that.”
#
# Leo looks at Flynn in disbelief, folding his arms. Flynn shrugs, putting the lighter away.
# “Hey, I said quit smoking cigarettes.”
