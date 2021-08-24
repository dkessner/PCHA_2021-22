---
layout: page
title: 1.1-1.2 Unit Circle, Trig Graphs
permalink: /1.1-1.2_unit_circle_trig_graphs/
---

I'll be posting class notes and supplementary material for each lesson. 

![](notes_example.png)

Here's a warmup: what's going on in this interactive demo?

<div class="sketch-container" id="unitCircleContainer"></div>    

<br/>

General sinusoid:
$$
    f(x) = a \sin(b(x-h)) + k
$$  


<script src="unit_circle.js"></script>

<script>
    let unitCircle = new p5(addHandlers(unitCircleSketchMaker), "unitCircleContainer");
</script>

