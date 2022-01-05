from tkinter import *
import tkinter.colorchooser
class PixelArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art")
        self.selected_color = None

        self.drawing_grid = Canvas(self.root)
        self.drawing_grid.grid(column=0, row=0, sticky=(N, W, E, S))

        self.pen_selected = False
        self.erase_selected = False
        grid_width = 20
        grid_height = 10
        cell_length = 50
        self.cells = []
        for r in range(grid_height):
            for c in range(grid_width):
                cell = Frame(self.drawing_grid, width=cell_length, height=cell_length, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)

                cell.grid(column=c, row=r)
                cell.bind('<Button-1>', self.cell_tapped)
                self.cells.append(cell)

        self.control_frame = Frame(self.root, height=cell_length)
        self.control_frame.grid(column=0,row=1, sticky=(N, W, E, S))

        self.new_button = Button(self.control_frame, text="new", command=self.on_new)
        self.new_button.grid(column=0, row=0)

        self.save_button = Button(self.control_frame, text="save", command=self.on_save)
        self.save_button.grid(column=2, row=0)

        self.pen_button = Button(self.control_frame, text="pen", command=self.on_pen)
        self.pen_button.grid(column=6, row=0)
        
        self.erase_button = Button(self.control_frame, text="erase", command=self.on_erase)
        self.erase_button.grid(column=10, row=0)
        

        self.selected_colorbox = Frame(self.control_frame, borderwidth=2, relief=RAISED)
        self.selected_colorbox.grid(column=15, row=0, sticky=(N, W, E, S))

        self.pick_color_button = Button(self.control_frame, text="pick color", command=self.on_pick_color)
        self.pick_color_button.grid(column=18, row=0)

        cols, rows = self.control_frame.grid_size()
        for col in range(cols):
            self.control_frame.columnconfigure(col, minsize=cell_length)

        self.control_frame.rowconfigure(0, minsize=cell_length)

    def cell_tapped(self, event):
        widget = event.widget
        cell_idx = self.cells.index(widget)
        cell = self.cells[cell_idx]
        if self.pen_selected and self.selected_color != None:
            cell.configure(bg=self.selected_color)
        if self.erase_selected:
            cell.configure(bg="white")

    def on_new(self, *args):
        for cell in self.cells:
            cell.configure(bg="white")
        
        self.pen_selected = False
        self.erase_selected = False
        self.selected_color = None
        self.selected_colorbox.configure(bg="white")

    def on_erase(self, *args):
        self.erase_selected = True
        self.erase_button.configure(relief=SUNKEN)
        self.pen_button.configure(relief=RAISED)
        self.pen_selected = False
        
    def on_save(self, *args):
        pass

    def on_pen(self, *args):
        self.pen_selected = True
        self.erase_selected = False
        self.erase_button.configure(relief=RAISED)
        self.pen_button.configure(relief=SUNKEN)

    def on_pick_color(self, *args):
        color = tkinter.colorchooser.askcolor()
        print(color)
        if color[1] != None:
            self.selected_colorbox.configure(bg=color[1])
        self.selected_color = color[1]
        print(self.selected_color)

    
if __name__ == "__main__":
    root = Tk()
    app = PixelArtApp(root)
    root.mainloop()