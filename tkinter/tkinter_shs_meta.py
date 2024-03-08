
import tkinter

window = tkinter.Tk()
window.geometry("1000x1000")

canvas = tkinter.Canvas(window,width="500",height="500",relief="solid",bd=2)


meta = canvas.create_polygon(440,274,478,280,507,289,553,290,601,293,623,302,648,320,671,347,674,351,691,363,711,371,730,378,745,387,754,398,759,409,763,425,760,442,756
                                ,453,744,466,726,482,720,493,717,508,718,518,722,536,729,556,748,603,761,656,765,676,763,690,758,701,748,712,738,720,728,724,712,725,290,726
                                ,267,722,255,716,243,704,238,692,235,680,235,662,236,651,237,636,239,620,243,607,250,592,258,580,268,566,277,549,284,531,287,514,285,494,282
                                ,481,279,467,272,453,264,441,255,426,247,412,240,398,237,385,239,372,243,358,250,347,260,337,271,329,286,325,295,324,312,323,324,323,343,322
                                ,354,321,364,315,370,310,378,302,386,294,398,286,412,280,425,275,430,274,434,274,437,274,fill="#B7A0CE",outline='black', width=4)
meta_e = canvas.create_oval(440,365,445,370,fill="black",width=2)
meta_e2 = canvas.create_oval(570,380,575,385,fill="black",width=2)
meta_m = canvas.create_line(406,400,410,402,414,404,420,406,425,408,430,409,437,411,445,413,450,414,457,415,464,416,470,417,478,418,485,419,495,420,505,421,516,421,524,422
                            ,537,423,546,423,558,423,568,423,578,423,584,423,592,422,597,422,601,421,width=3)

canvas.pack()


canvas.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
window.mainloop()

#캔버스 메타몽