# Assignment Report: Mini Calculator
**Course:** Computer Science Fundamentals & Career Pathways  
**Course Code:** ETCCCP105  
**Faculty:** Rajesh Kumar  
**Author:** Raman raj shrivastava

---

## 1. Introduction
This assignment involves building a mini project using Visual Studio Code, Git, and GitHub to demonstrate practical development and collaboration tools. The chosen project is a command-line Mini Calculator developed in Python. The goal is to create a functional program, maintain it under version control, and provide proper documentation and a submission report.

## 2. Project Description & Objectives
The Mini Calculator performs basic arithmetic operations: addition, subtraction, multiplication, division. It also supports modulus, power, and square root operations. The objectives include:
- Implement operations with input validation.
- Maintain operation history to demonstrate file I/O.
- Document development steps and repository structure.
- Show use of Git commands and produce meaningful commit messages.

## 3. Tools Used
- Visual Studio Code: Code editing and debugging.
- Git: Version control (init, add, commit, branch, push).
- GitHub: Repository hosting and collaboration.
- Python 3: Programming language for the calculator.

## 4. Program Design
The program uses a simple menu-driven loop. Helper functions (add, sub, mul, div) encapsulate logic.

A `history.txt` file logs operations with timestamps for traceability. The `.gitignore` excludes runtime files.

## 5. How to Run
1. Clone the repository to your machine.
2. Open in VS Code.
3. Run `calculator.py` in the terminal.
4. Use the menu to perform operations.

## 6. Git Workflow & Commits
During development, at least five meaningful commits were made representing logical steps:
- Initial commit with base code.
- Input validation added.
- History logging added.
- Error handling improvements.
- Documentation and final cleanup.

Example git commands:
```
git init
git add .
git commit -m "Initial commit - added calculator.py"
git commit -m "Add input validation and history logging"
git commit -m "Improve error handling and messages"
git commit -m "Add README and docs"
git push -u origin main
```

## 7. Screenshots / Output
A sample terminal output screenshot is included in `screenshots/`.

## 8. Future Work
Potential extensions include GUI, unit tests, additional math features, and collaborative GitHub workflow with branches and pull requests.

## 09. Conclusion
This project demonstrates the end-to-end workflow required for the assignment: development in VS Code, version control with Git, hosting on GitHub, documentation, and a clear report.

---

