# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-05 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=64, unique=True)),
                ('height', models.DecimalField(blank=True, decimal_places=0, max_digits=14, null=True)),
                ('merkle_root', models.CharField(blank=True, max_length=64, null=True)),
                ('time', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('bits', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('nonce', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('version', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('in_longest', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('size', models.DecimalField(blank=True, decimal_places=0, max_digits=14, null=True)),
                ('chain_work', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('tx_count', models.DecimalField(decimal_places=0, max_digits=10)),
                ('prev_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_blocks', related_query_name='next_block', to='explorer.Block')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Orphan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=64)),
                ('orphan_hash', models.CharField(max_length=64, unique=True)),
            ],
        ),

        migrations.CreateModel(
            name='Datadir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dirname', models.CharField(max_length=2000)),
                ('blkfile_number', models.IntegerField(blank=True, null=True)),
                ('blkfile_offset', models.IntegerField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=64, db_index=True)),
                ('version', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('locktime', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('size', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('time', models.DecimalField(blank=True, db_index=True, decimal_places=0, max_digits=20, null=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='txs', related_query_name='tx', to='explorer.Block')),
                ('valid', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TxIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scriptsig', models.BinaryField(blank=True, null=True)),
                ('sequence', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('tx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tx_ins', related_query_name='tx_in', to='explorer.Tx')),
                ('position', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TxOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=0, max_digits=30)),
                ('position', models.DecimalField(decimal_places=0, max_digits=10)),
                ('scriptpubkey', models.BinaryField(blank=True, null=True)),
                ('spent', models.BooleanField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tx_outs', related_query_name='tx_out', to='explorer.Address')),
                ('tx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tx_outs', related_query_name='tx_out', to='explorer.Tx')),
                ('valid', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='txin',
            name='txout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tx_ins', related_query_name='tx_in', to='explorer.TxOut'),
        ),
    ]
