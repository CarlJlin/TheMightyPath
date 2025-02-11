public class Rogue extends Character{
    public Rogue() {
        super(35, 45, 25, 4, 3, 25,
                6, 5, 2, 2, 1, 3);
    }

    @Override
    public String getClassName() {
        return "Rogue";
    }
}