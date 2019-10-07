#include "modelview.h"

#include <Qt3DExtras/Qt3DWindow>
#include <Qt3DExtras/QForwardRenderer>
#include <QQuaternion>
#include <Qt3DCore/QEntity>
#include <Qt3DCore/QTransform>
#include <Qt3DRender/QCamera>
#include <Qt3DRender/QMesh>
#include <Qt3DRender/QPointLight>
#include <Qt3DExtras/QCuboidMesh>
#include <Qt3DExtras/QPhongMaterial>

#include <QDebug>

ModelView::ModelView(QWidget *parent)
   : QWidget(parent)
{
    QTextStream(stdout) << "std out \n";
    qDebug("debug");
    qInfo("info");
    qWarning("warning");
    qCritical("critical");

    auto view = new Qt3DExtras::Qt3DWindow();

    // create a container for Qt3DWindow
    container = createWindowContainer(view,this);

    // background color
    view->defaultFrameGraph()->setClearColor(QColor(QRgb(0x575757)));

    // Root entity
    auto rootEntity = new Qt3DCore::QEntity();

    // Camera
    auto cameraEntity = view->camera();
    cameraEntity->lens()->setPerspectiveProjection(55.0f, 16.0f/9.0f, 0.1f, 1000.0f);

    cameraEntity->setPosition(QVector3D(0, 0, 3.0f));
    cameraEntity->setUpVector(QVector3D(0, 1, 0));
    cameraEntity->setViewCenter(QVector3D(0, 0, 0));

    Qt3DCore::QEntity *lightEntity = new Qt3DCore::QEntity(rootEntity);
    Qt3DRender::QPointLight *light = new Qt3DRender::QPointLight(lightEntity);
    light->setColor("white");
    light->setIntensity(1);
    lightEntity->addComponent(light);
    Qt3DCore::QTransform *lightTransform = new Qt3DCore::QTransform(lightEntity);
    lightTransform->setTranslation(cameraEntity->position());
    lightEntity->addComponent(lightTransform);

    //Moth mesh
    Qt3DCore::QEntity * mothMeshEntity = new Qt3DCore::QEntity();

    Qt3DRender::QMesh *mothMesh = new Qt3DRender::QMesh();
    mothMesh->setSource(QUrl(QStringLiteral("X:/Prog/GitProjects/DataMoth/data_viewer/QT_Cpp/Rafale_Data_Viewer/MothHullSimplifiedUnit.obj")));

    mothMeshEntity->addComponent(mothMesh);

    // Cuboid
    auto cuboidMesh = new Qt3DExtras::QCuboidMesh();

    // CuboidMesh Transform
    auto cuboidTransform = new Qt3DCore::QTransform();
    //cuboidTransform->setScale(100.0f);
    cuboidTransform->setScale(1.0f);
    cuboidTransform->setTranslation(QVector3D(0.0f, 0.0f, 0.0f));
    cuboidTransform->setRotation(QQuaternion(1,1.5,1,0).normalized());

    auto cuboidMaterial = new Qt3DExtras::QPhongMaterial();
    cuboidMaterial->setDiffuse(QColor(QRgb(0x55AA88)));

    // assamble entity
    auto cuboidEntity = new Qt3DCore::QEntity(rootEntity);
    //cuboidEntity->addComponent(cuboidMesh);
    cuboidEntity->addComponent(mothMesh);
    cuboidEntity->addComponent(cuboidMaterial);
    cuboidEntity->addComponent(cuboidTransform);

    qDebug() << "mesh status: ";
    qDebug() << mothMesh->status();
    qDebug() << mothMesh->isEnabled();
    mothMesh->dumpObjectInfo();
    // Set root object of the scene
    view->setRootEntity(rootEntity);
}

void
ModelView::resizeView(QSize size)
{
    container->resize(size);
}

void
ModelView::resizeEvent ( QResizeEvent * /*event*/ )
{
  resizeView(this->size());
}
