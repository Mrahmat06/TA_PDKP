class userService(object):


  def __init__(self, kpop_store_item):
    kpop_store_item.geometry("350x950")
    kpop_store_item.title("Album Online Store - Item")
    Label(kpop_store_item, text="Silahkan pilih barang yang ingin anda beli").pack()
    radio_item = IntVar()
    R1 = Radiobutton(kpop_store_item, text="Harry Styles - Harry's House (2022)", variable=radio_item, value=1).place(x=75, y=50) 
    lb1 = Label(kpop_store_item, text = "Rp.280.000,00").place(x = 75,y = 80)  
    R2 = Radiobutton(kpop_store_item, text="Harry Styles - Fine Line (2019)", variable=radio_item, value=2).place(x=75, y=150) 
    lb1 = Label(kpop_store_item, text = "Rp.250.000,00").place(x = 75,y = 180) 
    R3 = Radiobutton(kpop_store_item, text="Harry Styles - Harry Styles (2017)", variable=radio_item, value=3).place(x=75, y=250) 
    lb1 = Label(kpop_store_item, text = "Rp.250.000,00").place(x = 75,y = 280)
    btn2 = Button(kpop_store_item, command = struk, text="SUBMIT").place(x=150,y=855)