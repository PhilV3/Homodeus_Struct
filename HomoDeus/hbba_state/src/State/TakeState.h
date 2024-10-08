#ifndef HD_TAKE_STATE_H
#define HD_TAKE_STATE_H

#include "State.h"

class TakeState : public State, public DesireSetObserver
{
    uint64_t m_takeDesireId;

public:
    TakeState(
        StateManager& stateManager,
        std::shared_ptr<DesireSet> desireSet,
        ros::NodeHandle& nodeHandle,
        std::type_index nextStateType);
    ~TakeState() override;

    DECLARE_NOT_COPYABLE(TakeState);
    DECLARE_NOT_MOVABLE(TakeState);

    void onDesireSetChanged(const std::vector<std::unique_ptr<Desire>>& _) override;

protected:
    void enable(const std::string& parameter, const std::type_index& previousStageType) override;
    void disable() override;
    std::type_index type() const override;

private:
    std::string generateObjectToTake(const std::string& parameter);
};

inline std::type_index TakeState::type() const
{
    return std::type_index(typeid(TakeState));
}

#endif