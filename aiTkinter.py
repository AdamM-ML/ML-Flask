import tkinter as tk
from tkinter import *
from tkinter import Tk
import re  # regex, regular expression functions
import webbrowser
import tkinter.scrolledtext as scrolledtext
import time


# ADDITIONAL FUNCTIONS
def destroyMainLoop():
    root.destroy()


def close():
    txt.mark_set("insert", "%d.%d" % (1, 1))
    txt.configure(state="normal")
    txt.insert(INSERT,
               "\n Goodbye!!!\n\n")
    txt.configure(state="disabled")
    txt.pack()
    root.after(1000, destroyMainLoop)


def clearTextInput():
    txt.configure(state="normal")
    txt.mark_set("insert", "%d.%d" % (1, 1))
    txt.delete("1.0", END)
    txt.configure(state="disabled")


def clearEntryInput():
    writing_field.delete(0, END)


def defaultLink():
    print("nothing to show")


def defragLink():
    webbrowser.open("https://www.ccleaner.com/defraggler")


def mailLink():
    webbrowser.open(
        "https://www.microsoft.com/pl-pl/microsoft-365/outlook/email-and-calendar-software"
        "-microsoft-outlook")
    webbrowser.open("https://www.google.com/intl/pl/gmail/about/")


def microsoftLink():
    webbrowser.open("https://www.microsoft.com")


def antiLink():
    webbrowser.open(
        "https://www.antivirusguide.com/best-antivirus/?lp=default&utm_source=google&utm_medium"
        "=cpc&sgv_medium=search&"
        "utm_campaign=6478205166&utm_content=77388860386&utm_term=%2Bantivirus&cid=380751417542"
        "&pl=&feeditemid=&targetid"
        "=aud-754909914386:kwd-30524480&mt=b&network=g&device=c&adpos=&p1=&p2=&geoid=1011320"
        "&gclid=CjwKCAiA2O39BRBjEiwAp"
        "B2Iksz29cm-Q50PufAiZkQ2g0KNT5UR_Npplq2KgTv-3TT0rEnN6fDP0hoCTAoQAvD_BwE")


def centerWindow(w=300, h=200):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2) - 35
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def showTime():
    timeResp = time.strftime('%H:%M:%S')
    return timeResp


# --ROOT WINDOW------------------- + fields

root = Tk()
root.title('Chatbot')
# root.geometry("1600x1000")
centerWindow(root.winfo_screenwidth() - 150, root.winfo_screenheight() - 150)
root.configure(background="ghost white")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='images/iconchat.ico'))

greetings_field = Label(root, height=6, bg="#f2e3ff",
                        text="\nHello. I am here to help you understand how you can use the "
                             "computer"
                             " to do various things like sending e-mails, using editing tools, "
                             "using applications "
                             "to do your work, but also to help you with computer maintenance "
                             "like finding good antivirus "
                             "or explaining how you can update your computer. I have no time for "
                             "questions concerning other"
                             " topics so please be concise and concrete.\n"
                             "Write your questions in the field below.\n",
                        font=("Verdana", 14), fg="black", wraplength=900)
greetings_field.pack(pady=8)

writing_field = Entry(root, font=("Verdana", 22), width=80, relief='solid', highlightthickness=7,
                      highlightbackground="purple3")
writing_field.pack()

txt = scrolledtext.ScrolledText(root, height=12, undo=True, font=("Verdana", "14"),
                                relief='solid', highlightthickness=2,
                                highlightbackground="OrangeRed4")
txt.configure(padx=190, bg="white", spacing1=2, spacing2=3, spacing3=2, wrap=WORD, state="disabled")
txt.pack(expand=True, fill='both', pady=12)


# ---------FUNCTIONS----------------

def Match():
    clear_counter = 0

    # Looking for particular requests

    # MAINTENANCE REQUESTS ------------------------------------

    find = re.search("[U|u]pdate", writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " --> System update means keeping your software up to date, it contains "
                   "security improvements, "
                   "\napplications support, sometimes even user interface(layout/GUI) changes."
                   "\nIt is very important to keep track of all system updates and perform the "
                   "update process often."
                   "\nIt is not only important for the overall functioning of your computer"
                   "\nbut also to prevent your computer from being attacked by viruses or malware."
                   "\nTo check if there are updates available for your system, go to the 'Settings'"
                   " (Windows) or 'Preferences' (MacOS) of your system"
                   "\n\nThere are updates for the particular applications too.\n"
                   " - In the case of the applications installed by you, you will have to update "
                   "them (if it is possible) from inside the application\n"
                   " - In the case of default applications of your system, then they update along"
                   " with you system update\n so they does not have to be updated one by one\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search("[A|a]ntivirus|[P|p]rotect|[P|p]rotecting|[V|v]iruses|[P|p]rotection",
                     writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " --> To protect your computer from malware, viruses or other software which "
                   "is meant to harm your computer"
                   " you have to install antivirus. There are free applications that you can "
                   "download and install, "
                   "but also paid ones, that may offer more functions than just protection ("
                   "functions like "
                   "checking drivers of your components and searching for updates). "
                   "I will open the webpage with the list of possible antiviruses for you. If you "
                   "want to"
                   " view it click 'Read more' button below.\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = antiLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search("[D|d]efragmentation|[D|d]efragment", writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " --> It is a very important process for your computer that has to be "
                   "performed from time to time. "
                   " During the usage of the disk, it becomes fragmented, so you must perfom "
                   "defragmentation sometimes. There is "
                   "no a specific time period specified."
                   " Defragmentation is basically a process of organizing the disk data in the "
                   "proper way"
                   " - it organizes the whole disk into "
                   "the number of small, adjacent regions/fragments. "
                   "I found the webpage where you can download a tool for it. If you want to view "
                   "it click 'Read more' button below\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defragLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search("[L|l]agging|[D|d]elay|[L|l]ag", writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " --> If your computer works with a delay, or works slower than usually, "
                   "it may have few reasons:\n"
                   " - Your system is not updated\n"
                   " - You have very little space on your hard disk\n"
                   " - There are some heavy processes working in background\n"
                   " - You started a process that has too high requirements for your computer"
                   "\n e.g. you may have too low-end graphics card in case of some"
                   "\n videogames delays - so it may be the case of your computer's components\n "
                   "that"
                   " are too weak for the process/application that causes the delay\n"
                   "===================================\n"
                   )
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    # VIDEOGAMES REQUESTS ------------------------------------

    find = re.search(
        "[H|h]ow can (I|i) play (computer)? ((?:a\s)|(?:the\s))*(videogame(s)?|game(s)?)|[H|h]ow "
        "to play (computer)? ((?:a\s)|(?:the\s))*(game(s)?|videogame(s)?) |videogame",
        writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " -->  To play games on your computer firstly you have to check, before buying "
                   "the game,"
                   " if your computer meets minimum requirements of the game (even better if it "
                   "meets 'recommended requirements')."
                   " Such information is usually given on the "
                   "back side of the box or on the webpage with the product (in case of buying "
                   "digital keys / activation keys)"
                   ". If it does not meet the requirements, there is no point in buying such a "
                   "game since it will not start,"
                   " or will start and will run horribly. However if it meets the requirements, "
                   "then you buy and install it. "
                   "During the installation process you will be asked where to install the game. "
                   "Install all games on one"
                   " chosen disk, in one chosen folder named for instance: games. Then you can "
                   "easily find the game folder"
                   " in the future and also check how much disk space is taken by all your games "
                   "by inspecting only one folder."
                   " If you want to start a game, go to game folder and find .exe file which "
                   "indicates that it is the application."
                   " It will always contain game logo as icon so it is easy to spot it. Other "
                   "method is to search in 'start menu'"
                   " in case of Windows, or 'Applications' folder in case of MacOs. "
                   "In case of MacOs all applications should be present in 'Launchpad' also.\n"
                   "If the game does not launch, or gives an error message then you should "
                   "investigate it on your own by searching for the solution for the particular "
                   "problem in the internet. It usually helps. "
                   "\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search(
        "[H|h]ow can (I|i) (uninstall|remove|delete|(dispose of)) ((?:a\s)|(?:the\s))*(videogame("
        "s)?|game(s)?)|[H|h]ow to (uninstall|remove|delete|(dispose of)) ((?:a\s)|(?:the\s))*("
        "videogame(s)?|game(s)?)",
        writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " -->  To delete the videogame from disk in Windows, go to"
                   " 'Control Panel' (type it in search box in bottom left corner) and click on "
                   "'Uninstall program'. Then look for"
                   " the one you want to remove and click uninstall.\n"
                   "In the case of MacOs go to 'Applications' folder and move"
                   " the application to trash. Do not forget to empty the trash after it."
                   "\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    # EDITING TOOLS REQUESTS / Other useful tools ------------------------------------

    find = re.search(
        "[B|b]rowser|[W|w]eb browser|[I|i]nternet search|explore internet|[I|i]nternet exploration",
        writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " -->  If you want to browse the internet you need a good web browser"
                   " for it. I recommend Google Chrome which is the most popular and has lots of "
                   "extensions ("
                   "additional software that does many different things e.g. extension for"
                   " blocking advertisements). Download your new web browser application using "
                   "your current one"
                   " - usually the default web browser of your system (Internet Explorer for "
                   "Windows or Safari for MacOS)\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search(
        "[M|m]ail|[E|e]-mail|[E|e]mail|[E|e]-message|send message|[M|m]essage|[M|m]essages|send",
        writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " --> Well, there are many ways to send messages/e-mails through the internet."
                   " You can use the following webmails to communicate:\n"
                   ": Gmail\n"
                   ": Outlook\n"
                   "There are many more of course but those two are the most popular, so that may "
                   "mean that they are the best right?\n"
                   "So to pick one of them, click 'Read more' and I will transport you to the "
                   "official webpages where you can create the account or log in to the existing "
                   "account"
                   ". Creating the account on Gmail may be the best choice since many online "
                   "shops, forums, "
                   "or generally webpages that require creating account to use them, have the "
                   "option to skip creating account process and log in "
                   "using your Gmail account, that is very handy when you do not have time to "
                   "create account, you just click \"log in with gmail\" and that's it. "
                   "Now to use your new mail account, you have to log in using information you "
                   "gave during registration like username and password "
                   "and then you can start messaging. Remember to give your messages a proper and "
                   "valid email address of the"
                   " receiver, otherwsie the message will not go through. Remember also to give "
                   "an adequate title of the message, so that "
                   "the receiver knows what the message is about. In your messages you can attach "
                   "files from your storage/hard disk.\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = mailLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search(
        "document|documents|write|writing|written|[P|p]aperwork|[P|p]aper work|[D|d]ocument "
        "editing|[E|e]diting documents|[E|e]dit documents|[R|r]eport|[A|a]rticle|[R|r]eview",
        writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " --> To create a document in which you can write you must"
                   " have a tool for it. Some systems like Windows offer ready to use document "
                   "editors like WordPad, or the ones that"
                   " you can buy like Microsoft Office (or other Microsoft tools e.g. for making "
                   "presentations"
                   " - Microsoft PowerPoint or reports/statistics - Microsoft Excel). "
                   "\nOther free document editors are available: \n - Google Docs which you can "
                   "use in web browser \n "
                   "- Libre Office Writer \n"
                   " - or even Microsoft Office products online - in web browser for free. "
                   "\nOn MacOS there are Pages and Keynote applications,"
                   " but you can also use mentioned Microsoft document "
                   "editors here because they are adapted to Mac system. "
                   "Nowadays you do not have to download and install editors"
                   " on your personal computer, you just need web browser and internet connection "
                   "to use online editors. That is very handy especially when"
                   " you work with somebody else. You can then share the document"
                   " via link or add a collaborant that can edit the same document "
                   "as you do and see all the changes instantly along with the information who "
                   "did them."
                   " If the work was only on your local computer, then each time"
                   " you make a change, you would have to send it to the person who"
                   " helps you. To use Microsoft online tools that I mentioned,"
                   " you must have the account, which can be easily created by going"
                   " to Microsoft webpage (if you want to go there now click 'Read more' button)."
                   " Once you have the account you can use these tools online.\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = microsoftLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search(
        "[M|m]usic|[L|l]istening to music|[L|l]isten to music|[C|c]reate my (own)? music|["
        "C|c]ompose my (own)? music",
        writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " -->  If you want to listen to music you have to use either of the following "
                   "programs:\n"
                   " - Winamp\n"
                   " - MediaMonkey\n"
                   " - MusicBee\n"
                   " - iTunes - only for Mac\n"
                   "Those are my suggestions, I tried some of them, other ones I heard of, "
                   "but basically all of them are ok. Very often you will not need any special "
                   "software to play the music since operating systems have built in applications "
                   "that do it. Just double click the music file you want to listen to. "
                   "Of course if it does not find any program that can play it, then download one "
                   "of those that I mentioned. However if you want to CREATE or COMPOSE music "
                   "yourself, then I am happy to present you more information. \n\n"
                   "I used FL Studio a long time and I can totally recommend it to you. There is "
                   "one minus however (in the ocean of pluses) - you have to buy it to use it "
                   "legally. As far as I know all software that "
                   "enables you to create or edit music is not cheap e.g. Adobe Audition which "
                   "you have to spend almost 1000PLN on...\n"
                   "Here are my suggestions:\n"
                   " - FL Studio - they say (and I say) it is the best. Available for Mac and "
                   "Windows. \n"
                   " - Apple Logic Pro - available for Mac. \n"
                   " - There is GarageBand on Mac as default also but well... It is not very "
                   "professional. \n"
                   " - Adobe Audition - very professional software. It can have a monster "
                   "performance when you know how to use its full potential\n\n"
                   "There are some free music creation applications like Cakewalk or SyndtSphere "
                   "which are not bad, they are ok for beginners or for simple tasks, but I would "
                   "mainly recommend the ones I mentioned above if you look for professional "
                   "performance.\n"
                   "===================================\n"
                   )
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search(
        "[P|p]ainting(s)?|[D|d]raw(ing)?|[A|a]rtwork|[P|p]aint|[H|h]ow to paint|[H|h]ow to make ("
        "?:a\s)*painting|[H|h]ow to create ((?:an\s)|(?:the\s))*artwork|[C|c]reate ((?:an\s)|("
        "?:the\s))*(artwork|painting)|digital art",
        writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " -->  Creating paintings using a computer program requires different skills "
                   "than painting on paper. Being a good painter/artist while creating your work "
                   "on paper, does not mean you will perform good using software and in reverse.\n"
                   "There are many tools you can use to create digital art:\n"
                   " - Photoshop CC - Adobe product, for Mac and Windows, as almost all Adobe "
                   "products it is expensive and requires knowledge how to use it to discover its "
                   "true potential. Used for both editing pictures/photos but also to create "
                   "artwork\n"
                   " - Affinity Designer - that is my recommendation if you want to create "
                   "designs or illustrations if you used some artwork software before. That is "
                   "because it requires some acquaintance in using such programs\n"
                   " - Artweaver 7 - good for beginners in the field of digital art\n"
                   " - Krita - free software.\n"
                   " - MediBang Paint Pro - free. Mostly to create comics\n"
                   " - Paintstorm Studio - for professionals in digital art. It is quite cheap in "
                   "comparison to its capabilities so I can recommend it.\n"
                   "There are a lot more but most of them are very expensive"
                   " like Corel Painter 2020 which costs around 400$. If you just want to do it "
                   "for fun or your own personal use then try out the ones I mentioned or just "
                   "use Krita which is free. However "
                   "if you want to publish your work somewhere and get money out of it, "
                   "I would recommend either using free software, or paying for the one you use "
                   "since if you get illegal version, you may have issues with law if somebody "
                   "discovers that your work was done on not original version of software.\n"
                   "Before you buy one of those paid programs, try out those that are free, "
                   "perhaps they will be enough for you, maybe you will be satisfied with what "
                   "they offer, so there will be no need to buy other programs\n"
                   "===================================\n"
                   )
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search("[P|p]hoto(graph(s)?)?|[P|p]hotos|[P|p]icture(s)?",
                     writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " --> It always comes down to the question whether you want to get tools for "
                   "professional job or for personal use. Software for editing photos "
                   "can be either for beginners or for professionals. Here are my suggestions:\n"
                   " - Adobe products:\n"
                   "   # Photoshop (for professionals)\n"
                   "   # Lightroom Classic (for professionals)\n"
                   "   # Photoshop Elements (for all, does not require much knowledge about "
                   "editing)\n"
                   "Very good thing about Adobe products is that there are"
                   " tutorials showing how to operate in those programs so it is easy to discover "
                   "its functionalities. Most Adobe products are available for both platforms: "
                   "Windows and MacOs\n"
                   " - GIMP - considered as the best free photo editor on the market, "
                   "but requires experience in editing (for MacOs and Windows)\n"
                   " - Paint.NET - free photo editor, good for beginners and advanced users ("
                   "Windows only)\n"
                   " - PhotoScape X - free software for all kinds of users. Easy to use + "
                   "available for MacOs and Windows\n"
                   "Before you buy photo editing software, try out those that are free, "
                   "perhaps they will be enough for you, maybe they will be able to do the "
                   "editing you want, so there will be no need to buy other programs.\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search(
        "[V|v]ideo editing|[V|v]ideo editor|[V|v]ideo(s)?|[M|m]ovie[a-z]?|[M|m]ovie[a-z]? "
        "editing|[M|m]ovie[a-z]? editor|[F|f]ilm[a-z]? editing|[F|f]ilm[a-z]? editor",
        writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " -->  If you want to play a video you have to use either of the following "
                   "programs:\n"
                   " - VLC media player - one of the best players available for both Mac and "
                   "Windows.\n"
                   " - 5Kplayer \n"
                   "That is basically all you need to know about playing videos. Very often you "
                   "will not need any special software to play the video since operating systems "
                   "have built in applications that do it. Just double click the video you want "
                   "to play. "
                   "Of course if it does not find any program that can play it, then download one "
                   "of those that I mentioned. However if you want to CREATE or EDIT videos "
                   "yourself, then I am happy to present you more information. \n\n"
                   "Video editing or short movies creation can be much easier with the use of the "
                   "following programs:\n"
                   " - OpenShot Video Editor - free to download and use. \n"
                   " - Blender - available for all platforms (Windows, Mac, Linux), also free. \n"
                   " - Lightworks. \n"
                   " - HitFilm Express - free, but requires professional knowledge about video "
                   "editing and techniques such as adding effects or proper clipping. \n"
                   " - iMovie - Mac video editor. \n"
                   " - VSDC - Windows video editor. \n"
                   " - Machete Lite - for quick, not very complicated editing.\n \n"
                   "If you know at least something about video editing, then you should have no "
                   "problems operating in all those editors (maybe apart from HitFilm Express). I "
                   "am sure you can find concrete and precise tutorials on Youtube "
                   "for each of the programs I mentioned.\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    # DEFAULT BEHAVIOUR-------------------------------------------------

    find = re.search("^$", writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   "How can I help you?\n"
                   "===================================\n"
                   )
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    # GENERAL ------------------------------------

    find = re.search("do it", writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   " Do what?\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    find = re.search("([H|h]i)|([H|h]ello)|([H|h]ey)|([W|w]elcome)", writing_field.get())
    if find and clear_counter != 1:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT,
                   "Hello. As I said, I am here to help you understand how you can use the computer"
                   " to do various things like sending e-mails, using editing tools, "
                   "using applications "
                   "to do your work, but also to help you with computer maintenance like finding "
                   "good antivirus "
                   "or explaining how you can update your computer. I have no time for questions "
                   "concerning other topics so please be concise and concrete.\n"
                   "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()

    if clear_counter == 0:
        txt.mark_set("insert", "%d.%d" % (1, 1))
        txt.configure(state="normal")
        txt.insert(INSERT, "\n -- " + writing_field.get() + "  (at: " + showTime() + ")" + "\n")
        txt.pack()
        txt.insert(INSERT, "I do not know that\n"
                           "===================================\n")
        txt.configure(state="disabled")
        txt.pack()
        LinkButton['command'] = defaultLink
        clear_counter = clear_counter + 1
        clearEntryInput()


# BUTTONS------------------------------------

askBtn = PhotoImage(file='images/ask.png')
readBtn = PhotoImage(file='images/readmore.png')
clearBtn = PhotoImage(file='images/clearwindow.png')
exitBtn = PhotoImage(file='images/exitBtn.png')

AskButton = Button(root, font="Helvetica 22 bold italic",
                   text="Ask", image=askBtn, width=229, height=72, command=Match, borderwidth=0)
AskButton.pack(pady=8)

LinkButton = Button(root, font="Helvetica 13 bold italic",
                    text="Read more", image=readBtn, width=174, height=63, command=defaultLink,
                    borderwidth=0)
LinkButton.pack(pady=8)

ClearButton = Button(root, font="Helvetica 13 italic",
                     text="Clear conversation window", image=clearBtn, width=243, height=48,
                     command=clearTextInput, borderwidth=0)

ClearButton.pack(pady=8)

ExitButton = Button(root, font="Helvetica 13 italic", text="Exit", image=exitBtn, width=132,
                    height=60, command=close, borderwidth=0)
ExitButton.pack(anchor='sw', pady=8, padx=8)

# BINDING KEY TO THE BUTTON

root.bind('<Return>', (lambda event: Match()))

# LOOPING TKINTER
root.mainloop()
