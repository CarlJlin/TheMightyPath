public abstract class Character {
    private final int baseAtk;
    private final int baseHp;
    private final int baseRes;
    private final int baseMana;
    private final int baseMagic;
    private final int baseAgi;
    private final double growthAtk;
    private final double growthHp;
    private final double growthRes;
    private final int growthMana;
    private final int growthMagic;
    private final double growthAgi;
    private int level;
    private int exp;
    private int expToNextLevel;
    private double difficulty = 1.2;

    public Character(int baseAtk, int baseHp, int baseRes, int baseMana, int baseMagic, int baseAgi,
                     double growthAtk, double growthHp, double growthRes, int growthMana, int growthMagic, double growthAgi) {
        this.baseAtk = baseAtk;
        this.baseHp = baseHp;
        this.baseRes = baseRes;
        this.baseMana = baseMana;
        this.baseMagic = baseMagic;
        this.baseAgi = baseAgi;
        this.growthAtk = growthAtk;
        this.growthHp = growthHp;
        this.growthRes = growthRes;
        this.growthMana = growthMana;
        this.growthMagic = growthMagic;
        this.growthAgi = growthAgi;
        this.level = 1;
        this.exp = 0;
        this.expToNextLevel = 100;
    }

    public double getStat(Stats stat, int level) {
        return switch (stat) {
            case Str -> baseAtk + growthAtk * level;
            case Hp -> baseHp + growthHp * level;
            case Res -> baseRes + growthRes * level;
            case Mana -> baseMana + growthMana * level;
            case Magic -> baseMagic + growthMagic * level;
            case Agi -> baseAgi + growthAgi * level;
            default -> throw new IllegalArgumentException("Unknown stat: " + stat);
        };
    }

    public void selectDifficulty(String chosenDifficulty) {
        switch (chosenDifficulty) {
            case "easy" -> setDifficulty(1.2);
            case "normal" -> setDifficulty(1.4);
            case "hard" -> setDifficulty(1.8);
            case "hardcore" -> setDifficulty(2.5);
            default -> throw new IllegalArgumentException("Unknown difficulty: " + chosenDifficulty);
        }
    }

    public void setDifficulty(double difficulty) {
        this.difficulty = difficulty;
    }

    public abstract String getClassName();

    public void levelUp() {
        if(exp >= expToNextLevel) {
            level++;
            exp -= expToNextLevel;
            expToNextLevel = (int) (expToNextLevel * difficulty);
        }
    }
}
