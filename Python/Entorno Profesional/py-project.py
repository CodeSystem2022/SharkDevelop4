import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200,34,120]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')

    plt.close()

# main.py
import charts

def run():
    charts.generate_pie_chart()

if __name__ =='__main__':
    run()
