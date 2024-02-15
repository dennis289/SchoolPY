# a prompt to the user to input credentials
RatePerHour=float(input("Enter hourly rate"))
HoursWorked=int(input("Enter the hours worked"))
# The workoutdone using the inputed credentials
GSalary= (RatePerHour*HoursWorked)
# printing the gross pay
print("The gross salary is: ")
print(GSalary)
