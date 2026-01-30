class dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        
    def info(self):
        print(f'Name is: {self.name} || Age: {self.age}')

    def __str__(self):
        return f'{self.name} is {self.age} year.'
    
def main():
    mydog = dog('Buddy',3)
    mydog.info()
    your_dog = dog('Diddy',2)
    print(your_dog)

if __name__ == "__main__":
    main()