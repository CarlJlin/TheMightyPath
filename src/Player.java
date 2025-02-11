import java.util.HashMap;
import java.util.Map;

public class Player {
    private String name;
    private Map<Class<? extends Character>, Integer> classLevels;
    private Character currentClass;

    public Player(String name) {
        this.name = name;
        this.classLevels = new HashMap<>();
    }

    public void chooseClass(Character characterClass) {
        if (!classLevels.containsKey(characterClass.getClass())) {
            classLevels.put(characterClass.getClass(), 1);
        }
        this.currentClass = characterClass;
    }

    public void levelUpCurrentClass() {
        if (currentClass != null) {
            Class<? extends Character> currentClassType = currentClass.getClass();
            int newLevel = classLevels.get(currentClassType) + 1;
            classLevels.put(currentClassType, newLevel);
        }
    }

    public int getCurrentClassLevel() {
        return currentClass != null ? classLevels.get(currentClass.getClass()) : 0;
    }

    public double getStat(Stats stat) {
        return currentClass != null ? currentClass.getStat(stat, getCurrentClassLevel()) : 0;
    }

    public String getName() {
        return name;
    }

    // Example of how player can have stats:
    public void displayStats() {
        System.out.println("Name: " + name);
        System.out.println("Current Class: " + (currentClass != null ? currentClass.getClassName() : "None"));
        System.out.println("Class Level: " + getCurrentClassLevel());
        for (Stats stat : Stats.values()) {
            System.out.println(stat + ": " + getStat(stat));
        }
    }
}
