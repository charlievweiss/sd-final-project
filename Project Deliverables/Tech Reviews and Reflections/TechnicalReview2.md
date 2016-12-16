# sd-final-project
[link to presentation deck](https://docs.google.com/presentation/d/1QSa4f5D_WXPZvMMHYrlKtpmf6gs_WBpuDCIzktKduQI/edit?usp=sharing)

## Background and context

Skateboarders have very specific preferences as to how their boards feel and handle. Each boarder’s unique style drives their requirement for how stiff their board is. In addition, different skateboarders vary in weight; decks that are too stiff for a light rider could be too flexible for a heavy one. Currently, riders chasing the perfect board have to rely on brute-force experimentation, buying multiple decks to find one with the perfect stiffness.

Our project is a tool that takes in rider weight and riding style and generates a skateboard geometry for the user to take to a laser cutter or 3D cad program. The skateboards our code designs are fiberglass laminated medium-density fiberboard, with hexagonal patterns cut out of the fiberboard to determine the stiffness of the board.

![Board Example]
(https://static1.squarespace.com/static/563a3237e4b023d5f8284d31/57f456c7b3db2b8bb9b5dc70/57f45f29e3df28be9827fe9a/1475632943058/DB5CF4A4-9224-4A0E-BC89-BF720C3D4BC9.JPG?format=1000w)

Currently, our project is organized into three major components =
A flask WebApp that collects user data and allows the user to download their completed skateboard, a python model which takes the collected user data and computes the desired hexagonal pattern based on test data, and a python function which calls a CAD program called OpenScad to draw hexagons and exports a .dxf cad file.

Going forward, we'd like to better develop our user interface as per the feedback from our first technical review, try and prepare for deployment to the web in some way, and most critically modify our OpenScad-interfacing code to draw a full skateboard instead of a single hexagon element.

## Key questions

- Now that we have some code written and a better idea of what we're doing and our dependencies, how do can we best deploy this to the web without forcing a major redesign?
- One of our big problems is that OpenScad does not support splines or equation driven curves. Is there a way to produce splines using other, simpler geometry?
- How do we render a webpage that takes POST requests and handles file display simultaneously?
- What are some bad practices in our code?
- Where are our biggest risks? What are we overlooking right now?

## Agenda for technical review session

- Review the skateboard product and variables that affect its functionality (2 minutes)
- Provide explanation of the software architecture, current and planned (5 minutes)
- Demo project (5 minutes)
- Review Code & Ask key questions (10 minutes)
- Gather feedback on program risks we may be missing(5 minutes)
- Q&A (3 minutes)
