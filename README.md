# Defining the problem 

Горила Джекі із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків (piles) з бананами, 
у і-тому кошику є певна кількість бананів Х. Кошики знаходяться під охороною, але охорона здійснює обхід 
зоопарку на Н годин, протягом якого Джекі може поласувати своєю улюбленою стравою. Джекі може з'їсти за
 годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть К бананів звідти. Якщо кошик має менше, 
 ніж К бананів, вона з'їдає всі банани з нього і більше не буде їсти бананів протягом цієї години. Джекі любить 
 їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш ніж охоронці повернуться. Визначіть 
 мінімальне ціле число К таким чином, щоб Джекі могла з'їсти всі банани на складі протягом Н годин, поки повернеться 
 охорона.
 <br>
 </br>
 
 Constraints :
  - 1 <= piles.length <= 10^4
  - piles.length <= H <= 10^9
  - 1 <= piles[i] <= 10^9
  
  Example 1
  
  Input: piles = [3,6,7,11], H = 8 <br>
  Output: 4
  
  Example 2 
  
  Input: piles = [30,11,23,4,20], H = 5 <br>
  Output: 30
  
  Example 3
  
  Input: piles = [30,11,23,4,20], H = 6 <br>
  Output: 23
  
  #Logic behind implementation
  The solution uses binary search to find the smallest speed of consumption that satisfies 
  time boundary given in the task. 
  Main components of execution:
  - determining low and high limits for binary search (optimises the algorithm time complexity)
  - running binary search itself to find optimal speed 
  - checking predicted speed to determine whether it's fast enough to not overflow predefined time boundary
  <br>
  An explicit walk-through the algorithm is provided alongside with the code 
  
  # Complexity analyses 
  
  - Space complexity O(1)
  - Time complexity O(nlog(m))
      
      - n is the number of piles <br>
      - m is total amount of bananas in piles <br>
 
  
  
  
  