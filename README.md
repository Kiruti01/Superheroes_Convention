# Superheroes_Convention

You are organizing the next comic book convention in the famous San Diego Convention Center. Because of a new virus the convention will be just a 2-day event.

Each superhero will have his stand but there is a big problem: They dont want to share the space with superheros they hate. For example, if Batman hates Superman, you can't put them on the same day. You may put Batman stand on day 1 and Superman stand on day 2.

Based on that, your team has given you a database for all superheroes assisting which superheroes they hate. Your job is to tell your team if it is possible to organize all the superheroes in these 2 days without sharing the place with heroes they don't like.
Be aware that hundreds of superheros attend the convention, so you should optimize your algorithm!

Assumptions: For simplicity (but not necessity/sufficiency)

Suppose the hate is mutual, so if Spiderman hates Captain America then Captain America hates spiderman.
Assume the superheroes dont have depression, i.e. they dont hate themselves.
Input:(dictionary) You will be receiving a Dictionary, each key is a superhero ID and its value is a list of superheroes IDs he/she hates. If the superhero doesn't hate anyone, the value is an empty list.

Output:(boolean) True if it's possible to organize all the superheroes in these 2 days without sharing the space with superheroes they hate, otherwise False.

Example:
Input: {0:[1, 2], 1: [0], 2: [0], 3: []}
Dont get confused, the above superhero IDs dictionary is equivalent to:
{"Superman":["Batman", "Aquaman"], "Batman": ["Superman"], "Aquaman": ["Superman"], "Wonderwoman": []}

Output: True.
One combination of organizing them is: Batman and Aquaman on day 1 and Superman on day 2. Wonderwoman has no conflicts so she could go any day
