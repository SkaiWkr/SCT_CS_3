#!/usr/bin/env python3
import argparse, tkinter as tk, math, re
from tkinter import ttk

def assess_password(password):
    checks = {
        'Length (8+)': len(password) >= 8,
        'Uppercase': bool(re.search(r'[A-Z]', password)),
        'Lowercase': bool(re.search(r'[a-z]', password)),
        'Numbers': bool(re.search(r'\d', password)),
        'Special chars': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    # Calculate character set size
    charset_size = 0
    if checks['Lowercase']: charset_size += 26
    if checks['Uppercase']: charset_size += 26
    if checks['Numbers']: charset_size += 10
    if checks['Special chars']: charset_size += 32
    
    # Time to crack calculation (50% of keyspace, 1B attempts/sec)
    if charset_size > 0:
        combinations = charset_size ** len(password)
        seconds = combinations / (2 * 1e9)
        crack_time = format_time(seconds)
    else:
        crack_time = "Instantly"
    
    score = sum(checks.values())
    strength = 'Strong' if score >= 4 else 'Medium' if score >= 2 else 'Weak'
    color = '#4CAF50' if score >= 4 else '#FF9800' if score >= 2 else '#F44336'
    
    return checks, strength, color, crack_time, score

def format_time(seconds):
    if seconds < 1: return "< 1 second"
    if seconds < 60: return f"{seconds:.0f} seconds"
    if seconds < 3600: return f"{seconds/60:.0f} minutes"
    if seconds < 86400: return f"{seconds/3600:.0f} hours"
    if seconds < 31536000: return f"{seconds/86400:.0f} days"
    if seconds < 31536000000: return f"{seconds/31536000:.0f} years"
    return f"{seconds/31536000:.0e} years"

def create_gui(password, checks, strength, color, crack_time, score):
    root = tk.Tk()
    root.title("Password Strength Analysis")
    root.configure(bg='#1e1e1e')
    root.geometry('400x350')
    root.resizable(False, False)
    
    # Header
    tk.Label(root, text="🔐 Password Strength", font=('Arial', 16, 'bold'), 
             fg='#ffffff', bg='#1e1e1e').pack(pady=15)
    
    # Strength display
    strength_frame = tk.Frame(root, bg='#1e1e1e')
    strength_frame.pack(pady=10)
    
    tk.Label(strength_frame, text=f"Strength: {strength}", font=('Arial', 14, 'bold'),
             fg=color, bg='#1e1e1e').pack()
    
    # Progress bar
    progress = ttk.Progressbar(strength_frame, length=200, value=score*20, 
                              style='custom.Horizontal.TProgressbar')
    progress.pack(pady=5)
    
    # Crack time
    tk.Label(root, text=f"⏱️ Time to crack: {crack_time}", font=('Arial', 12),
             fg='#ffeb3b', bg='#1e1e1e').pack(pady=10)
    
    # Criteria checklist
    criteria_frame = tk.Frame(root, bg='#2d2d2d', relief='raised', bd=1)
    criteria_frame.pack(pady=15, padx=20, fill='x')
    
    tk.Label(criteria_frame, text="Security Criteria:", font=('Arial', 11, 'bold'),
             fg='#ffffff', bg='#2d2d2d').pack(pady=(10,5))
    
    for criteria, passed in checks.items():
        icon = "✅" if passed else "❌"
        color_text = '#4CAF50' if passed else '#F44336'
        tk.Label(criteria_frame, text=f"{icon} {criteria}", font=('Arial', 10),
                 fg=color_text, bg='#2d2d2d', anchor='w').pack(pady=2, padx=15, fill='x')
    
    tk.Label(criteria_frame, text="", bg='#2d2d2d').pack(pady=5)
    
    # Style the progress bar
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('custom.Horizontal.TProgressbar', background=color, 
                   troughcolor='#3d3d3d', borderwidth=0, lightcolor=color, darkcolor=color)
    
    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description='🔐 Analyze password strength', 
                                   formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('password', help='Password to analyze')
    args = parser.parse_args()
    
    print(f"\033[95m🔐 Analyzing password strength...\033[0m")
    checks, strength, color, crack_time, score = assess_password(args.password)
    print(f"\033[92mLaunching GUI analysis...\033[0m")
    
    create_gui(args.password, checks, strength, color, crack_time, score)

if __name__ == "__main__":
    main()
