public class Cleric extends Character{
    public Cleric() {
        super(5, 40, 15, 60, 15, 7,
                1.5, 4, 2, 10, 3, 2);
    }

    @Override
    public String getClassName() {
        return "Cleric";
    }
}