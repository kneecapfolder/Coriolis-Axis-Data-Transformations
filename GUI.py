import customtkinter as tk

class AppInterface:
    def __init__(self):
        self.root = tk.CTk()
        self.root.geometry(f'{310}x{615}')
        self.root.title('Remote Desktop Control')
        self.root.resizable(False, False)
        
        self.canvas1 = tk.CTkCanvas(self.root, width=300, height=300, bg='white')
        self.canvas1.pack(pady=5)
        
        self.canvas2 = tk.CTkCanvas(self.root, width=300, height=300, bg='white')
        self.canvas2.pack(pady=5)



    def start(self):
        # Run app
        self.root.mainloop()


    def draw_point(self, canvas : tk.CTkCanvas, x, y, t):
        canvas.delete('all')

        canvas.create_text(30, 10, text=f't={t:.4f}', fill='blue', font=("Arial", 10, "bold"))

        # Draw Axis
        canvas.create_line(0, 150, 300, 150, arrow=tk.LAST, width=2, fill="black")
        canvas.create_line(150, 300, 150, 0, arrow=tk.LAST, width=2, fill="black")

        canvas.create_aa_circle(x*4+150, 150-y*4, 4, 360, 'red')
        