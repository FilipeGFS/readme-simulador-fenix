# FÊNIX MODEL ROCKET SIMULATOR 🚀

![Fênix logotype](https://scontent.fplu1-1.fna.fbcdn.net/v/t1.6435-9/158499275_124854939643696_884025964079056168_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=e3f864&_nc_ohc=lOiVht85iucAX8OUZSa&_nc_ht=scontent.fplu1-1.fna&oh=00_AfAD0aDwQ5xpZectX7LwkavHNh4Q9nKiNUzxGW8aiksQZQ&oe=63B172A4)

This program is a free and open access simulator for model rocketry. With this software, the user will be able to simulate their rocket as a rigid body, 
obtaining important data about it, such as drag force, different drag coefficient types, the position of center of pression, trajectory expected, stress
data and so much more. By reading this document, you are going to be able to understand how to use this simulator, as well as what it calculates, what inputs 
it needs and what outputs it returns.
Thus, this document will be divided in the following topics, defined according to the folders and archives of the project:
+ Data
+ Utils
+ Physics
+ Aerodynamic
+ Propulsion
+ Recovery
+ Structure
+ Simulation

### Data
The data folder contains some primordial information for the project, with files in JSON format. It is subdivided in folders with the type of data of the 
following table:
| Folder | Content |
| ------ | ------- |
| Cables | Types of cables |
| Materials | Several materials for the model and its properties, such as aluminum, carbon fiber, etc. |
| Parachutes | Different kinds of parachute, depending on its geometry, with the info of its drag coefficient |
| Propellants | Three distinct propellant types with their trcnical features |


![image](https://user-images.githubusercontent.com/119083049/205334940-a6ef751c-301f-4e05-b510-16c5f3a45f61.png)

*Example of data in 'materials' folder*

![image](https://user-images.githubusercontent.com/119083049/205336259-ce7237fa-ceeb-457c-a856-0b738c8cc93a.png)

*Example of data in 'propellants' folder*

### Utils
In 'utils', we have important content simulation, like archives which contain classes for grouping related data, like parachute, nose type, rocket parts
data. We also have codes with fundamental constants needed and wind information for simulation.

![image](https://user-images.githubusercontent.com/119083049/205337747-80985d27-a945-499e-a02b-516676f5e25f.png)

*Parachute class code*

![image](https://user-images.githubusercontent.com/119083049/205337967-7099a96a-3698-4480-b9dd-23fade6ae09e.png)


*Wind direction class code*

### Physics

### Aerodynamic

### Propulsion

### Recovery

### Structure
The Structure folder holds codes for the calculus of diverse tension and stress types, as well as of information got from the input dimensions of the
rocket and safety margin. Next, we will describe each code archive of this folder, its inputs and outputs.

#### 1. *Parameter a* code
Inputs: 
+ **'external_radius'**
+**'internal_radius'**
+**'vessel_maximum_pressure'**
+**'von_Mises_stress'**

Outputs: 
+ **'parameter_a'**: the relation between motor external and internal radius.

This property of the motor can be calculated by different ways using different combinations of the inputs. Therefore, not all inputs are necessary.
The manners to calculate the 'parameter a' are shown below:

![image](https://user-images.githubusercontent.com/119083049/205346674-7cdf4c3e-b032-44c7-82db-42ae27ae9daf.png)

*Code for calculus of parameter a.*

#### 2. *Thin walls check* code
Inputs:
+ **'external_radius'**
+**'internal_radius'**

Outputs:
+**'thickness'**: difference between external radius and internal radius

This technical feature will be important for some following calculus and is determined this way:

![image](https://user-images.githubusercontent.com/119083049/205354985-0f1eefdf-2225-4bfc-b759-3568199f8080.png)

#### 3. *Circumferential tension* code
Inputs:
+ **'parameter_a'**: the relation between motor external and internal radius.
+ **'vessel_maximum_pressure'**: maximum pressure inside motor due to ignition of fuel grain.

Outputs:
+ **'circumferential_tension'**

This code calculates the circumferetial tension expected to act on motor thin walls.

#### 4. *External radius* code
Inputs:
+ **'parameter_a'**
+ **'internal_radius'**

Outputs:
+ **'external_radius'**

As you might imagine, this code returns the external radius for the motor of the rocket.

#### 5. *Longitudinal tension* code
Inputs:
+ **'parameter_a'**
+ **'vessel_maximum_pressure'**

Outputs:
+ **'longitudinal_tension'**: the longitudinal tension that will act on motor thin walls.

This parameter is important to know if the motor walls will resist the tension applied to it, and it is calculated with the following 
expression:

$VMP / (2*(a - 1))$

*VMP: 'Vessel Maximum Pressure'*

#### 6. *Radial tension* code
Inputs:
+ **'parameter_a'**
+ **'vessel_maximum_pressure'**

Outputs:
+ **0**: radial tension in motor considered to have thin walls is always zero.

With a thin walls motor, this function always returns 0.

#### 7. *Von Mises stresss* code
Inputs:
+ **'parameter_a'**
+**'vessel_maximum_pressure'**
+**'safety_margin'**
+**'material'**: material used to build the motor

Output:
+ **'von_Mises_stress'**: von Mises stress calculated in it's own method

For this calculus, the safety margin is not a necessary input. Once the safety margin depends on Von Mises stress for being calculated, the
Von Mises Stress will be recalculated after obtaining the safety margin. Said that, this parameter is acquired this way:

![image](https://user-images.githubusercontent.com/119083049/205353417-75907c1f-12d4-4e3c-816e-9c52e512e312.png)

*Von Mises stress calculus*


#### 8. *Safety margin* code
Inputs:
+ **'von_Mises_stress'**
+ **'material'**

Outputs: 
+ safety_margin of the built motor

The safety margin is important to ensure that the motor will resist the Von Mises stress. It is calculated as in the next picture:

![image](https://user-images.githubusercontent.com/119083049/205365465-fa6fc29d-c934-4e6b-b135-8a4dd89e27c1.png)


*Safety margin calculus*

#### 9. *Thickness* code
Inputs:
+ **'external_radius'**
+**'internal_radius'**

With all these methods, we're able to determine a lot of important things for simulation and for checking rocket properties.


### Simulation
This folder is responsible for creating objects and abstract classes indispensable for the simulation and for making the simulations itself.
Its activities are accomplished by the codes that will be described next.

#### 1. *Abstract ambient* code
This file creates a superclass for the other ambients needed. It receives a list of forces for the construction of the ambient. 

#### 2. *Airless earth ambient* code
It generates a subclass of AbstractAmbient which comprehends an environment of an airless earth and uses the *'physics'* codes.

![image](https://user-images.githubusercontent.com/119083049/205357761-2600c612-d2b9-4ef1-85f3-0ed59c2f1cc8.png)

*Airless earth code*

#### 3. *Earth ambient* code
Just as the other classes, this is a subclass of AbstractAmbient. It is similar to the previous file, but this Earth has a 'little' difference:
it has atmosphere.

![image](https://user-images.githubusercontent.com/119083049/205358530-b8f7d806-fe50-475a-9817-c9e44d52eeec.png)

*Airfull Earth code*

#### 4. *Simulation* code
This is the most extensive code of this folder and is responsible for the simulation itself. in the 'simulation' class, it coordinates the physics
simulation. This class has a lot of especial functions that will be briefly described in the ensuing table:

| Method | What it does |
| ------ | ------------ |
| setupForces() | adds the forces involved in the simulation |
| tryEjection() | verifies periodically if the parachute must be ejected in that moment and tries to do so |
| __correctParachuteOrientation() | after ejection, it corrects rocket's orientation to (0,0,1) |
| simulate() | runs the simulation for a specified range time and using a defined time interval |
| __applyResultantForce() | applies the resultant force on the body |
| __applyResultantTorque() | calculates and applies the resultant torque on the body |

With this part of the code, we're able to simulate properly, as we wanted.

### References used in this project

[1] Samuel Renan Costa Morais. Metodologia Para C ́alculo Estrutural de Motor de Foguete de Propelente S ́olido.
Belo Horizonte/MG, 2021.

[2] J. Barrowman. The practical calculation of the aerodynamic characteristics of slender finned vehicles. M.Sc.
thesis, The Catholic University of America, 1967.

[3] Sampo Niskanen. Openrocket technical documentation. Available at https://openrocket.info/
documentation.html (2021/11/10), 2013.

[4] Ma ́ıra Fernanda Oliveira de Miranda. DESENVOLVIMENTO DE UM SISTEMA DE RECUPERAC ̧AO ̃
PARA UM MINIFOGUETE, Uberlˆandia 2021.

[5] Gary Peek Jean Potvin. OSCALC: Opening Shock Calculator, julho 2006.











