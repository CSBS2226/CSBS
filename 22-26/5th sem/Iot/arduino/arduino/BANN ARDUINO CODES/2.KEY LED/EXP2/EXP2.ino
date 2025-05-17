

int led1 = 2;
int led2 = 3;
int led3 = 4;
int led4 = 5;

int key1 = 7;
int key2 = 8;
int key3 = 9;
int key4 = 10;

void setup()

{
       pinMode(led1, OUTPUT);
       pinMode(led2, OUTPUT);
       pinMode(led3, OUTPUT);
       pinMode(led4, OUTPUT);
       pinMode(key1, INPUT);
       pinMode(key2, INPUT);
       pinMode(key3, INPUT);
       pinMode(key4, INPUT);
     
         
          
            
}


void loop()

{

 if(digitalRead(key1)==1)
 {
   digitalWrite(led1, HIGH);
 }
 else
 {
   digitalWrite(led1, LOW);
 }

 if(digitalRead(key2)==1)
 {
   digitalWrite(led2, HIGH);
 }
 else
 {
   digitalWrite(led2, LOW);
 }
if(digitalRead(key3)==1)
 {
   digitalWrite(led3, HIGH);
 }
 else
 {
   digitalWrite(led3, LOW);
 }

 if(digitalRead(key4)==1)
 {
   digitalWrite(led4, HIGH);
 }
 else
 {
   digitalWrite(led4, LOW);
 }
}
