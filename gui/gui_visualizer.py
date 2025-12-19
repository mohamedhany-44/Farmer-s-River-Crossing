# gui_visualizer.py
import tkinter as tk
from tkinter import ttk
import time
from gui.M_problem import INITIAL_STATE
from gui.M_search_algorithms import bfs, dfs, astar

class RiverCrossingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Farmer's River Crossing Problem Solver")
        self.root.geometry("900x700")
        self.root.configure(bg="#2c3e50")
        
        self.current_step = 0
        self.solution_path = []
        self.animation_running = False
        
        # Title
        title_frame = tk.Frame(root, bg="#34495e", pady=15)
        title_frame.pack(fill=tk.X)
        tk.Label(title_frame, text="🚣 Farmer's River Crossing Problem 🚣", 
                font=("Arial", 20, "bold"), bg="#34495e", fg="white").pack()
        
        # Algorithm selection
        control_frame = tk.Frame(root, bg="#2c3e50", pady=10)
        control_frame.pack()
        
        tk.Label(control_frame, text="Select Algorithm:", 
                font=("Arial", 12), bg="#2c3e50", fg="white").grid(row=0, column=0, padx=5)
        
        self.algo_var = tk.StringVar(value="BFS")
        algo_menu = ttk.Combobox(control_frame, textvariable=self.algo_var, 
                                 values=["BFS", "DFS", "A*"], state="readonly", width=10)
        algo_menu.grid(row=0, column=1, padx=5)
        
        tk.Button(control_frame, text="🔍 Solve", command=self.solve, 
                 bg="#27ae60", fg="white", font=("Arial", 11, "bold"), 
                 padx=20, pady=5).grid(row=0, column=2, padx=10)
        
        tk.Button(control_frame, text="▶️ Play", command=self.play_animation, 
                 bg="#3498db", fg="white", font=("Arial", 11, "bold"), 
                 padx=20, pady=5).grid(row=0, column=3, padx=5)
        
        tk.Button(control_frame, text="⏸️ Pause", command=self.pause_animation, 
                 bg="#e67e22", fg="white", font=("Arial", 11, "bold"), 
                 padx=20, pady=5).grid(row=0, column=4, padx=5)
        
        tk.Button(control_frame, text="⏮️ Reset", command=self.reset, 
                 bg="#e74c3c", fg="white", font=("Arial", 11, "bold"), 
                 padx=20, pady=5).grid(row=0, column=5, padx=5)
        
        # Step controls
        step_frame = tk.Frame(root, bg="#2c3e50", pady=5)
        step_frame.pack()
        
        tk.Button(step_frame, text="◀️ Previous", command=self.prev_step, 
                 bg="#95a5a6", fg="white", font=("Arial", 10), padx=15).grid(row=0, column=0, padx=5)
        
        self.step_label = tk.Label(step_frame, text="Step: 0 / 0", 
                                   font=("Arial", 12, "bold"), bg="#2c3e50", fg="white")
        self.step_label.grid(row=0, column=1, padx=20)
        
        tk.Button(step_frame, text="Next ▶️", command=self.next_step, 
                 bg="#95a5a6", fg="white", font=("Arial", 10), padx=15).grid(row=0, column=2, padx=5)
        
        # Canvas for visualization
        self.canvas = tk.Canvas(root, width=850, height=400, bg="#87ceeb", highlightthickness=0)
        self.canvas.pack(pady=20)
        
        # Info panel
        info_frame = tk.Frame(root, bg="#34495e", pady=10)
        info_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        self.info_text = tk.Text(info_frame, height=8, font=("Courier", 10), 
                                bg="#ecf0f1", fg="#2c3e50", wrap=tk.WORD)
        self.info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.draw_initial_state()
    
    def draw_scene(self, state):
        """Draw the river crossing scene with current state"""
        self.canvas.delete("all")
        
        # Draw river
        self.canvas.create_rectangle(300, 0, 550, 400, fill="#1e90ff", outline="")
        self.canvas.create_text(425, 20, text="🌊 RIVER 🌊", 
                               font=("Arial", 16, "bold"), fill="white")
        
        # Draw banks
        self.canvas.create_rectangle(0, 0, 300, 400, fill="#90ee90", outline="")
        self.canvas.create_rectangle(550, 0, 850, 400, fill="#90ee90", outline="")
        
        self.canvas.create_text(150, 20, text="LEFT BANK", 
                               font=("Arial", 14, "bold"), fill="#2c3e50")
        self.canvas.create_text(700, 20, text="RIGHT BANK", 
                               font=("Arial", 14, "bold"), fill="#2c3e50")
        
        # Draw boat
        farmer_pos = state[0]
        if farmer_pos == "L":
            boat_x = 250
        else:
            boat_x = 600
        self.canvas.create_oval(boat_x-30, 180, boat_x+30, 220, 
                               fill="#8b4513", outline="#654321", width=2)
        self.canvas.create_text(boat_x, 200, text="🚣", font=("Arial", 20))
        
        # Entity positions and emojis
        entities = [
            ("Farmer", "👨‍🌾", state[0]),
            ("Fox", "🦊", state[1]),
            ("Goat", "🐐", state[2]),
            ("Cabbage", "🥬", state[3])
        ]
        
        left_entities = [e for e in entities if e[2] == "L"]
        right_entities = [e for e in entities if e[2] == "R"]
        
        # Draw entities on left bank
        for i, (name, emoji, _) in enumerate(left_entities):
            x = 80 + (i * 60)
            y = 250
            self.canvas.create_text(x, y, text=emoji, font=("Arial", 40))
            self.canvas.create_text(x, y+50, text=name, font=("Arial", 10, "bold"))
        
        # Draw entities on right bank
        for i, (name, emoji, _) in enumerate(right_entities):
            x = 630 + (i * 60)
            y = 250
            self.canvas.create_text(x, y, text=emoji, font=("Arial", 40))
            self.canvas.create_text(x, y+50, text=name, font=("Arial", 10, "bold"))
        
        # Draw safety warning if unsafe
        if not self.is_state_safe(state):
            self.canvas.create_text(425, 380, text="⚠️ UNSAFE STATE ⚠️", 
                                   font=("Arial", 16, "bold"), fill="red")
    
    def is_state_safe(self, state):
        """Check if state is safe"""
        farmer, fox, goat, cabbage = state
        if fox == goat and farmer != fox:
            return False
        if goat == cabbage and farmer != goat:
            return False
        return True
    
    def draw_initial_state(self):
        """Draw initial state"""
        self.draw_scene(INITIAL_STATE)
        self.update_info("Ready to solve! Select an algorithm and click 'Solve'.")
    
    def solve(self):
        """Solve the problem using selected algorithm"""
        self.animation_running = False
        algo_name = self.algo_var.get()
        
        self.update_info(f"Solving with {algo_name}...\n")
        
        # Get algorithm
        algorithms = {"BFS": bfs, "DFS": dfs, "A*": astar}
        algo = algorithms[algo_name]
        
        # Solve
        start_time = time.time()
        path, nodes = algo(INITIAL_STATE)
        end_time = time.time()
        
        if path:
            self.solution_path = path
            self.current_step = 0
            
            info = f"✅ Solution Found!\n\n"
            info += f"Algorithm: {algo_name}\n"
            info += f"Path Length: {len(path)-1} moves\n"
            info += f"Nodes Expanded: {nodes}\n"
            info += f"Time: {end_time - start_time:.6f} seconds\n\n"
            info += "Click 'Play' to animate or use Next/Previous to step through."
            
            self.update_info(info)
            self.update_step_display()
            self.draw_scene(path[0])
        else:
            self.update_info("❌ No solution found!")
    
    def play_animation(self):
        """Animate the solution"""
        if not self.solution_path:
            self.update_info("Please solve the problem first!")
            return
        
        self.animation_running = True
        self.animate_step()
    
    def animate_step(self):
        """Animate one step"""
        if not self.animation_running or self.current_step >= len(self.solution_path) - 1:
            self.animation_running = False
            return
        
        self.current_step += 1
        self.draw_scene(self.solution_path[self.current_step])
        self.update_step_display()
        
        self.root.after(1500, self.animate_step)
    
    def pause_animation(self):
        """Pause animation"""
        self.animation_running = False
    
    def next_step(self):
        """Go to next step"""
        if not self.solution_path:
            return
        
        if self.current_step < len(self.solution_path) - 1:
            self.current_step += 1
            self.draw_scene(self.solution_path[self.current_step])
            self.update_step_display()
    
    def prev_step(self):
        """Go to previous step"""
        if not self.solution_path:
            return
        
        if self.current_step > 0:
            self.current_step -= 1
            self.draw_scene(self.solution_path[self.current_step])
            self.update_step_display()
    
    def reset(self):
        """Reset to initial state"""
        self.animation_running = False
        self.current_step = 0
        self.solution_path = []
        self.draw_initial_state()
        self.step_label.config(text="Step: 0 / 0")
    
    def update_step_display(self):
        """Update step counter"""
        if self.solution_path:
            self.step_label.config(
                text=f"Step: {self.current_step} / {len(self.solution_path)-1}"
            )
    
    def update_info(self, text):
        """Update info panel"""
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = RiverCrossingGUI(root)
    root.mainloop()