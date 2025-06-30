# SCT_CS_3
# 🔐 Password Strength Analyzer

A sleek, dark-themed CLI tool with GUI visualization that analyzes password strength and estimates crack time using industry-standard security metrics.

## ✨ Features

- **CLI Interface**: Clean command-line interface with colored output
- **Dark Theme GUI**: Beautiful, modern dark interface using tkinter
- **Real-time Analysis**: Instant password strength assessment
- **Crack Time Estimation**: Calculates time needed to crack passwords using brute force
- **Security Criteria Check**: Validates against industry-standard password requirements
- **Visual Feedback**: Color-coded strength indicators and progress bars
- **Lightweight**: Zero external dependencies, uses only Python standard library

## 🛡️ Security Metrics

The tool evaluates passwords based on:

- **Length**: Minimum 8 characters recommended
- **Uppercase Letters**: A-Z character presence
- **Lowercase Letters**: a-z character presence  
- **Numbers**: 0-9 digit presence
- **Special Characters**: Symbols (!@#$%^&*(),.?":{}|<>)

## 🧮 Crack Time Calculation

Time estimation uses:
- **Character Set Size**: Based on actual character types used
- **Brute Force Assumptions**: 1 billion attempts per second
- **50% Rule**: Average case assumes 50% of keyspace needs to be searched
- **Modern Hardware**: Calculations reflect current computational capabilities

## 🚀 Installation & Usage

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Quick Start

1. **Clone or Download**
   ```bash
   git clone <repository-url>
   cd password-analyzer
   ```

2. **Run Analysis**
   ```bash
   python main.py "YourPassword123!"
   ```

3. **View Results**
   - CLI displays colored strength feedback
   - GUI window opens with detailed analysis

### Command Line Options

```bash
python main.py --help
```

## 📊 Strength Levels

| Strength | Criteria Met | Color Code | Security Level |
|----------|-------------|------------|----------------|
| **Weak** | 0-1 | 🔴 Red | High Risk |
| **Medium** | 2-3 | 🟠 Orange | Moderate Risk |
| **Strong** | 4-5 | 🟢 Green | Low Risk |

## 🎨 GUI Features

- **Dark Theme**: Easy on eyes with professional appearance
- **Progress Bar**: Visual strength representation
- **Criteria Checklist**: Clear pass/fail indicators
- **Crack Time Display**: Human-readable time estimates
- **Responsive Design**: Clean, modern interface

## 🔍 Technical Implementation

### Core Components

1. **Password Analysis Engine**
   - Regex pattern matching for character types
   - Comprehensive security criteria validation
   - Mathematical crack time calculations

2. **CLI Interface**
   - Argument parsing with argparse
   - Colored terminal output
   - Error handling and user feedback

3. **GUI Visualization**
   - Tkinter-based dark theme interface
   - Dynamic progress bars and styling
   - Real-time visual feedback

### Algorithm Details

**Character Set Calculation:**
```python
charset_size = 0
if lowercase_present: charset_size += 26
if uppercase_present: charset_size += 26  
if numbers_present: charset_size += 10
if symbols_present: charset_size += 32
```

**Crack Time Formula:**
```python
combinations = charset_size ^ password_length
seconds_to_crack = combinations / (2 * 1e9)
```

## 📈 Example Outputs

### Weak Password Example
```
Password: "password"
Strength: Weak (1/5)
Time to crack: 2 hours
Missing: Uppercase, Numbers, Special chars
```

### Strong Password Example
```
Password: "MyS3cur3P@ssw0rd!"
Strength: Strong (5/5)  
Time to crack: 2.3 × 10^15 years
All criteria met ✅
```

## 🎯 Use Cases

- **Personal Security**: Evaluate your own passwords
- **Educational Tool**: Learn about password security
- **Security Audits**: Quick password policy compliance checks
- **Development**: Integrate into larger security applications
- **Cybersecurity Training**: Demonstrate password vulnerabilities

## 🔒 Security Considerations

- **Local Processing**: Passwords never leave your machine
- **No Storage**: Tool doesn't save or log passwords
- **Memory Safe**: Passwords handled securely in memory
- **Offline Operation**: No network connections required

## 🤝 Contributing

Contributions welcome! Areas for enhancement:
- Additional character sets (Unicode, etc.)
- Dictionary attack simulation
- Password policy templates
- Export functionality
- API integration

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎓 Educational Value

This tool demonstrates:
- **Cybersecurity Principles**: Password security fundamentals
- **Python Programming**: CLI and GUI development
- **Mathematical Modeling**: Cryptographic time complexity
- **User Experience**: Clean interface design
- **Security Best Practices**: Safe password handling

## 📞 Support

For issues, questions, or contributions:
- Create an issue in the repository
- Review the code for customization options
- Check Python and tkinter documentation for troubleshooting

---

**Developed for cybersecurity education and personal security awareness.** 🛡️
