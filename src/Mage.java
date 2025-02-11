public class Mage extends Character{
    public Mage() {
        super(10, 35, 12, 50, 40, 5,
                1.5, 3.5, 1.5, 6, 5, 1.5);
    }

    @Override
    public String getClassName() {
        return "Mage";
    }

}