# Final Project - NBA Players

I will be using a small, personally generated data set of NBA players to study the the relationships between the players. 

Check out the Medium Post I wrote that dives deeper into the NBA and Graph Theory [here](https://medium.com/@timothy.kaing/nba-players-and-graph-theory-17362379aece)
---
The graph that I will be generating will have:

1. Vertice represents the NBA player
2. Edge represents their relation as teammates
3. The weight of each edge represents the years played together
---
By Developing this graph I hope to solve the 3 following problems: 

1. Player with the most teammates (Journeyman)
    1. Journeyman is defined as a “...worker or sports player who is reliable but not outstanding.”
    1. We can assume a player with a lot of unique teammates bounces between constant teams
2. Players that have the most chemistry
    1. Not necessarily true, but we can assume that the more years played together, the more chemistry that they share
3. Largest potential team of past/present teammates
    1. this is a clique? 
---
### Note

Using a basketball api is unfortunately out of scope for this project. "Years played together" is not a statistic easily accessible. To do so, I would have to compare the career stats between players to count the matching team/season.
