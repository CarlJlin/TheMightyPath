#pragma once
#include "hp.h"
#include "statBlock.h"

class Knight : public hp, public statBlock {

public:
	static const statType baseAttack = (statType)25u;
	static const statType AttackGrowth = (statType)5u;
	static const hptype HPGrowth = (hptype)6u;
	static const hptype baseHP = (hptype)60u;
	static const statType baseMana = (statType)5u;
	static const statType ManaGrowth = (statType)2u;
	static const statType baseRes = (statType)30u;
	static const statType ResGrowth = (statType)3u;
	static const statType baseMP = (statType)5u;
	static const statType MPGrowth = (statType)1u;
	static const statType baseAgi = (statType)10u;
	static const statType AgiGrowth = (statType)1u;

	Knight() : hp(baseHP, HPGrowth), statBlock(baseAttack, baseHP, baseRes, baseMana,baseMP,baseAgi) {


	};


private:


};