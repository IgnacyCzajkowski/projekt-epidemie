import main
import plot

liczba_symulacji = 3
file = open("C:\\Users\\Ignacy\\Desktop\\python\\algorytmy_genetyczne_2\\epidemie\\magistrala2.txt", 'w')
file.truncate()

for i in range(liczba_symulacji):
    print(liczba_symulacji - i)
    main.main()
plot.main()    