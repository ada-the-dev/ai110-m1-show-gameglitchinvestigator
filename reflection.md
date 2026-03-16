# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    Overall, the user interface was visually simple and intuitive. Upon running the application, values were not updated nor displayed correctly, the game's difficulty settings did not incrementally become more difficult, and hints based on the user's input (guesses) were given inconsistently. Not all input given by the user was displayed in the history data structure within the "developer debug info" window. The "New Game" button did not restart the game in a fresh state either.
- List at least two concrete bugs you noticed at the start (for example: "the hints were backwards").
    When increasing the game's difficulty from normal to hard, the numerical range for guessing values did not increase. When increasing the game's difficulty from easy to normal, the given attempts increased. I expect that the numerical ranges increase, and that the given attempts decrease when game difficulty increases.

    Adding on, the secret number for a game is not guarenteed to be within the range of that game's difficulty.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
