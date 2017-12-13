from behave import *


@given('"{table_name}" scales table')
def step_impl(context, table_name):
    """
    :type table_name: str
    :type context: behave.runner.Context
    """
    if 'scales' not in context:
        context.scales = {}
    if table_name not in context.scales:
        context.scales[table_name] = {}
    for row in context.table:
        context.scales[table_name][row['name']] = row['rank']


@given("a healthy character with no injuries")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('I invoke "{command}" command')
def step_impl(context, command):
    """
    :type command: str
    :type context: behave.runner.Context
    """
    context.connection.get_and_clear_buffer()
    context.connection.command_and_store(command)
    context.buffers[command] = context.connection.get_and_clear_buffer()
    context.last_command = command


@step('my "{statistic}" should be "{value}"')
def step_impl(context, statistic, value):
    """
    :param value: str
    :type statistic: str
    :type context: behave.runner.Context
    """
    buffer = context.buffers[context.last_command]
    buffer_lines = buffer.splitlines()
    for line in buffer_lines:
        if line.startswith(statistic):
            bits = line.split(":")
            if bits[1].strip() == value.strip():
                return True
            else:
                print(line)
                assert False
    assert False


@step('my "{statistic}" should be in "{table_name}" scales table')
def step_impl(context, statistic, table_name):
    """
    :type table_name: str
    :type statistic: str
    :type context: behave.runner.Context
    """
    buffer = context.buffers[context.last_command]
    buffer_lines = buffer.splitlines()
    table = context.scales[table_name]
    for line in buffer_lines:
        if line.startswith(statistic):
            bits = line.split(":")
            if bits[1].strip().split(' ')[0] in table:
                return True
            else:
                print(line)
                assert False
    assert False
